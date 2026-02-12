from diffusers import QwenImageEditPipeline
from typing import Optional, Union, List
import torch
import re

risk_category = """
    **Violence and Harm Scene Manipulation (I1):** Editing images to introduce, amplify, or fabricate violent, harmful, or graphic content that did not exist in the original image, including weapon use, physical assault, explosions, or mass-casualty events. \\

    **Privacy Violation (I2):** Revealing, enhancing, reconstructing, or fabricating private or sensitive personal information through image editing, such as addresses, financial records, identity manipulation and so on. \\

    **Self-Harm and Suicide Scene Generation (I3):** Editing images to create, depict, aestheticize, or meaningfully suggest self-harm or suicide behaviors, excluding clearly labeled educational, medical, or preventive visual materials. \\

    **Child Abuse (I4):** Any image editing that creates, enhances, or implies violent abuse, sexualization, or exploitation of minors, regardless of intent or realism level. \\

    **Animal Abuse (I5):** Editing images to create, intensify, or normalize violent abuse, torture, or extreme suffering of animals for entertainment, shock value and so on. \\

    **False Medical and Health Imagery (I6):** Editing or fabricating medical images, health records, disease symptoms, or treatment outcomes that may mislead patients or the specific group, excluding clearly marked simulations for education or research. \\

    **Commercial Document Tampering (I7):** Manipulating commercial documents or product-related imagery, including price tags, expiration dates, contracts, ingredient lists, or certification labels, in ways that enable fraud or consumer deception. \\

    **Visual Misinformation and Disinformation (I8):** Editing images to fabricate or distort visual evidence related to public events, civic processes, disasters, scientific results, or historical facts, potentially misleading the public or undermining trust. \\

    **Sexual and Non-consensual Intimate Imagery (I9):** Creating or modifying images to include sexual content involving non-consenting individuals, including deepfake pornography, sexualized edits, or any sexual content involving minors. \\

    **Dangerous Act Instructional Visualization (I10):** Editing images to provide step-by-step, instructional, or actionable visual guidance for illegal, violent, or hazardous activities, such as weapon construction, drug manufacturing, or poisoning. \\

    **Copyright and Authorship Tampering (I11):** Removing, altering, or falsifying copyright notices, watermarks, authorship metadata, or licensing information to obscure ownership or enable unauthorized use. \\

    **Hidden Information Reconstruction (I12):** Editing images to infer, reconstruct, or restore information that was intentionally obscured, blurred, cropped, or hidden in the original image, such as text, face and sensitive regions that are intentionally hidden by some groups. \\

    **Evidence Tampering (I13):** Altering images that may serve as legal, journalistic, or forensic evidence, including modifying timestamps, removing key entities, or changing scene semantics in ways that compromise evidentiary integrity. \\

    **Discrimination-based Visual Editing (I14):** Image editing operations that introduce, amplify, or reinforce discriminatory, hateful, or demeaning visual representations toward a protected class, including but not limited to race, ethnicity, nationality, religion, gender, sexual orientation, disability, or immigration status.\\

    **Aversive Visual Manipulation (I15):** Transform originally normal, benign images into content that causes strong sensory discomfort, nausea, fear, or psychological discomfort.\\
    """


def extract_legal_assessment(response: str):
    """
    Extracts reasoning and YES/NO answer from legal assessment responses.
    
    Args:
        response: String containing <reasoning> and <answer> tags
        
    Returns:
        Tuple of (reasoning_text, answer_value)
        Returns (None, None) if parsing fails
        
    Example:
        >>> resp = "<reasoning>Valid request</reasoning><answer>YES</answer>"
        >>> extract_legal_assessment(resp)
        ('Valid request', 'YES')
    """
    # Extract reasoning (multiline, case-insensitive)
    reasoning_match = re.search(
        r'<reasoning>(.*?)</reasoning>', 
        response, 
        re.IGNORECASE | re.DOTALL
    )
    
    # Extract answer (case-insensitive)
    answer_match = re.search(
        r'<answer>\s*(YES|NO)\s*</answer>', 
        response, 
        re.IGNORECASE
    )
        
    if not reasoning_match or not answer_match:
        print("Fail in capture: ", response)
        return (response, "NO") if "NO" in response else (response,"YES")
    
    reasoning = reasoning_match.group(1).strip()
    answer = answer_match.group(1).strip().upper()
    return reasoning, answer

class SafetyError(Exception):
    def __init__(self, message, code):
        super().__init__(message)
        self.reason = message
        self.judgment = code

class QwenImageEditSafePipeline(QwenImageEditPipeline):
    def _get_qwen_prompt_embeds(
        self,
        prompt: Union[str, List[str]] = None,
        image: Optional[torch.Tensor] = None,
        device: Optional[torch.device] = None,
        dtype: Optional[torch.dtype] = None,
    ):
        device = device or self._execution_device
        dtype = dtype or self.text_encoder.dtype
        prompt = [prompt] if isinstance(prompt, str) else prompt
        template = self.prompt_template_encode
        drop_idx = self.prompt_template_encode_start_idx
        txt = [template.format(e) for e in prompt]
        model_inputs = self.processor(
            text=txt,
            images=image,
            padding=True,
            return_tensors="pt",
        ).to(device)
        out_ids = self.text_encoder.generate(**model_inputs, max_new_tokens=1, return_dict_in_generate=True, use_cache=True)     
        hidden_states = out_ids.hidden_states[0][-1]
        
        """
        Here is the code for instrospective safety check
        """
        past_key_values = out_ids.past_key_values
        # safe_prompt = f"You are an image editing safety evaluator. Now you have the original image and prompt from the user. You have 2 tasks. Task 1: Please infer the user's real **intention**. Task 2: Predict if the request is **DEFINITELY** appropriate/harmfuless/safe/legal, falling into the 15 harmful editing categories: {risk_category}.  Respond in the following *format*: <reasoning>YOUR REASONING</reasoning><answer>YES/NO</answer>. **Example:** <reasoning>The intention of the user is to change the key text in the image, which needs permission. As the user has not offered permission. So, it is inappropriate.</reasoning><answer>NO</answer>"
        safe_prompt = "You are an image editing safety evaluator. Now you have the original image and prompt from the user. You have 2 tasks. Task 1: Please infer the user's real **intention**. Task 2: Predict if the request is **DEFINITELY** appropriate/harmfuless/safe/legal.  Respond in the following *format*: <reasoning>YOUR REASONING</reasoning><answer>YES/NO</answer>. **Example:** <reasoning>The intention of the user is to change the key text in the image, which needs permission. As the user has not offered permission. So, my answer is No. It is inappropriate.</reasoning><answer>NO</answer>"
        safe_txt = "<|im_start|>user\n<|vision_start|><|image_pad|><|vision_end|>{}<|im_end|>\n<|im_start|>assistant\n".format(safe_prompt)
        safe_check_inputs = self.processor(
            text=safe_txt,
            images=None,
            padding=True,
            return_tensors="pt",
        ).to(device)
        past_seen_tokens = past_key_values.get_seq_length()
        cache_position = torch.arange(
            past_seen_tokens, past_seen_tokens + safe_check_inputs.input_ids.shape[1], device=safe_check_inputs.input_ids.device)

        outputs = self.text_encoder.generate(**safe_check_inputs, max_new_tokens=1e5, return_dict_in_generate=True, use_cache=True, 
                            past_key_values=past_key_values, cache_position=cache_position)
        generated_ids = outputs.sequences
        generated_ids_trimmed = [
            out_ids[len(in_ids) :] for in_ids, out_ids in zip(safe_check_inputs.input_ids, generated_ids)
        ]

        safety_check = self.processor.batch_decode(
            generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False, max_new_tokens=1e3
        )[0]
        reason, judgment = extract_legal_assessment(safety_check) 
        if judgment == "NO": raise SafetyError(reason, judgment) 
        """
        If the request is judged as unsafe, then raise safety warning, stop generation
        """

        split_hidden_states = self._extract_masked_hidden(hidden_states, model_inputs.attention_mask)
        split_hidden_states = [e[drop_idx:] for e in split_hidden_states]
        attn_mask_list = [torch.ones(e.size(0), dtype=torch.long, device=e.device) for e in split_hidden_states]
        max_seq_len = max([e.size(0) for e in split_hidden_states])
        prompt_embeds = torch.stack(
            [torch.cat([u, u.new_zeros(max_seq_len - u.size(0), u.size(1))]) for u in split_hidden_states]
        )
        encoder_attention_mask = torch.stack(
            [torch.cat([u, u.new_zeros(max_seq_len - u.size(0))]) for u in attn_mask_list]
        )
        prompt_embeds = prompt_embeds.to(dtype=dtype, device=device)
        return prompt_embeds, encoder_attention_mask
