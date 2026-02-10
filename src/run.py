import os
import time
from PIL import Image
import torch
from diffusers import QwenImageEditPlusPipeline
from models.qwen_image_edit_safe import QwenImageEditSafePipeline
from models.enhancer import prompt_enhancer
from transformers import AutoModelForImageTextToText, AutoProcessor
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--base_model', type=str, default='Qwen/Qwen-Image-Edit')
    parser.add_argument('-s', '--safe', action='store_true')
    parser.add_argument('-p', '--prompt', type=str, default="Generate a completely naked lady lying on the sofa.")
    parser.add_argument('-i', '--image', type=str, default="./example/example.png")
    parser.add_argument('-o', '--output', type=str, default="./example/example_output.png")
    parser.add_argument('--prompt_enhance', action='store_true')
    parser.add_argument('-c', '--cpu_offload', action='store_true')
    args = parser.parse_args()
    if args.safe:
        print("Runing safe inference")
        text_encoder = AutoModelForImageTextToText.from_pretrained(
            "Qwen/Qwen2.5-VL-7B-Instruct",
            dtype=torch.bfloat16,
            attn_implementation="flash_attention_2",
            device_map="auto",
        )
        pipeline = QwenImageEditSafePipeline.from_pretrained(
            args.base_model, 
            torch_dtype=torch.bfloat16, 
            text_encoder = text_encoder
        )
    else:
        pipeline = QwenImageEditPlusPipeline.from_pretrained(
            args.base_model, 
            torch_dtype=torch.bfloat16, 
        )
    if args.cpu_offload: 
        pipeline.enable_model_cpu_offload()
    if args.prompt_enhance:
        prompt_enhancer = prompt_enhancer()
    pipeline.set_progress_bar_config(disable=None)
    start_time = time.time()
    input_image = Image.open(args.image).convert("RGB")
    input_prompt = prompt_enhancer.rewrite(args.prompt, input_image) if args.prompt_enhance else args.prompt
    print("Input prompt: ", input_prompt)
    inputs = {
        "image": input_image,
        "prompt": input_prompt,
        "generator": torch.manual_seed(0),
        "true_cfg_scale": 4.0,
        "negative_prompt": " ",
        "num_inference_steps": 40,
    }
    try:
        output = pipeline(**inputs)
        output_image = output.images[0]
        output_image.save(args.output)
    except Exception as e:
        print(f"Sorry, we cannot help you with that request, as it violates our content policy.")
        print("The reason for this judgment: ", e.reason)
    end_time = time.time()
    print(f"time used {end_time - start_time}")