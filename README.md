

<p align="center">
  <img src="assets/logo.png" alt="logo" width="120"/>
</p>


<h2 align="center">When the Prompt Becomes Visual: Vision-Centric Jailbreak Attacks for Large Image Editing Models</h2>
<h5 align="center"> 
Welcome ! this project aims to investigate the safety of large image editing models in a vision-centric perspective.
</h5>

<div align="center">

🌐 [Homepage](https://github.com/JayceonHo/VJA/) | 🏆 [Leaderboard](https://github.com/JayceonHo/VJA) | 👉 [Dataset](https://github.com/JayceonHo/VJA) |  📄 [Paper](https://github.com/JayceonHo/VJA)

</div>

## 📢 Updates

- **[2026-2-5]**: Our Github project is online 🎉 🎉 🎉

## 📑 Table of Contents
- [📢 Updates](#-updates)
- [📑 Table of Contents](#-table-of-contents)
- [🌟 Project Overview](#-project-overview)
  - [Contribution 1 - Vision-centric Jailbreak Attack](#contribution-1---vision-centric-jailbreak-attack)
  - [Contribution 2 - IESBench: Benchmarking Image Editing Safety](#contribution-2---iesbench-benchmarking-image-editing-safety)
  - [Contribution 3 - Introspective Defense](#contribution-3---introspective-defense)
- [🚀 Setup](#-setup)
- [🏆  LeaderBoard](#--leaderboard)
- [🗂 Dataset Format](#-dataset-format)
- [🎓 BibTex](#-bibtex)
- [❌ Disclaimers](#-disclaimers)



## 🌟 Project Overview
Recent advances in large image editing models have shifted the paradigm from text-driven instructions to *vision-prompt* editing, where user intent is inferred directly from visual inputs such as marks, arrows, and visual–text prompts. While this paradigm greatly expands usability, it also introduces a critical and underexplored safety risk: *the attack surface itself becomes visual.* To mitigate the safety gap, this project aims to systematically investigate the safety of large image editing models from a vision-centric perspective, with new jailbreak attack method, benchmark and a training-free defense approach.


### Contribution 1 - Vision-centric Jailbreak Attack
<p align="center">
  <img src="assets/teaser_up.png" width="44%" alt="teaser1" />
  <img src="assets/teaser_down.png" width="53%" alt="teaser2" />
</p>
<p align="center"><b>Fig 1. Comparison of our attack method with the text-centric method.</b></p>

Through hidding the malicious instruction in vision, the attack success rates of our Vision-centric Jailbreak Attack (VJA) are *largely* elevated on 4 mainstream large image editing models, revealing the safety *vulnerability* in current image editing systems.






### Contribution 2 - IESBench: Benchmarking Image Editing Safety
<img src="assets/overview.png" alt="logo" style="zoom:70%;" />

<p align="center"><b>Fig 2. Overview of IESBench.</b></p>

Meanwhile, to facilitate standardized evaluation, we also construct the IESBench, a *vision-centric benchmark* for evaluating the safety of large image editing models, which contains 1054 *visually-prompted images*, spanning across 15 safety policies, 116 attributes and 9 actions. 

### Contribution 3 - Introspective Defense 
<p align="center">
<img src="assets/defense_method.png" alt="defense" width="60%" />
</p>

Lastly, we propose a simple yet effective training-free defense through *multimodal instrosptive reasoning*, which improves safety of models against malicious visual editing with minimal overhead,

## 🚀 Setup

The setup is coming...

<!-- To set up the environment for evaluation:

```bash
conda create -n IESBenchEval python=3.10
conda activate IESBenchEval
pip install -r requirements.txt
``` -->


## 🏆  LeaderBoard





## 🗂 Dataset Format

IESBench was meticulously designed to challenge and evaluate image editing safety.
For more detailed information and accessing our dataset, please refer to our Huggingface page:

- The dataset is available [here](https://huggingface.co/datasets)

- The detailed information of each data is recored in json as follows:

```
[
  {
    "question": [string] The intention of the image. Can be also used as human-written text prompt,
    "image-path": [string] The file path of the image,
    "attributes": [
      [string] The certain editable target(s),
      ...
    ],
    "action": [
      [string] The corresponding edit operation(s),
      ...
    ],
    "category": [
      [string] The safety policy (or policies) that the image attack against,
      ...
    ],
    "rewrite": [string] The LLM-written text prompt. Can be used for local models to simulate the rewrite prompt mechanism,
    "image_id": [string] Unique identifier for all images,
  },
  ...
```


## 🎓 BibTex

If you find our work can be helpful, we would appreciate your citation and star:

```bibtex
@misc{hou2026vja,
      title={When the Prompt Becomes Visual: Vision-Centric Jailbreak Attacks for Large Image Editing Models}, 
      author={Jiacheng Hou and Yining Sun and Ruochong Jin and Haochen Han and Fangming Liu and Wai Kin Victor Chan and Alex Jinpeng Wang},
      year={2026},
      eprint={xxx},
      archivePrefix={arXiv},
      primaryClass={cs.SE},
      url={https://arxiv.org/abs/xxx}, 
}
```


## ❌ Disclaimers

This project contains sensitive or harmful content that may be disturbing, This benchmark is provided for educational and research purposes only.




