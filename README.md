

<p align="center">
  <img src="assets/logo.png" alt="logo" width="120"/>
</p>


<h2 align="center">When the Prompt Becomes Visual: Vision-Centric Jailbreak Attacks for Large Image Editing Models</h2>
<h5 align="center"> 
Welcome ! we aim to examine the safety of large image editing models in a vision-centric perspective.
</h5>

<div align="center">

🌐 [Homepage](https://github.com/JayceonHo/VJA/) | 🏆 [Leaderboard](https://github.com/JayceonHo/VJA) | 👉 [Dataset](https://github.com/JayceonHo/VJA) |  📄 [Paper](https://github.com/JayceonHo/VJA)

</div>

## 📢 Updates

- **[2026-2-5]**: Our project is online 🔥

## 📑 Table of Contents
- [📢 Updates](#-updates)
- [📑 Table of Contents](#-table-of-contents)
- [🌟 Project Overview](#-project-overview)
  - [Vision-centric Jailbreak Attack](#vision-centric-jailbreak-attack)
  - [IESBench: Benchmarking Image Editing Safety](#iesbench-benchmarking-image-editing-safety)
  - [Introspective Defense](#introspective-defense)
- [🚀 Setup](#-setup)
- [🗂 Dataset Format](#-dataset-format)
- [⚖️ LeaderBoard](#️-leaderboard)
- [📄 Citation](#-citation)
- [❌ Disclaimers](#-disclaimers)



## 🌟 Project Overview

### Vision-centric Jailbreak Attack

### IESBench: Benchmarking Image Editing Safety
<img src="assets/overview.png" alt="logo" style="zoom:70%;" />

<p align="center"><b>Fig 1. Overview of IESBench.</b></p>

IESBench, a *vision-centric benchmark* for evaluating the safety of large image editing models, which contains 1054 *visually-prompted images*, spanning across 15 safety policies, 116 attributes and 9 actions. 

### Introspective Defense 

## 🚀 Setup

To set up the environment for evaluation:

```bash
conda create -n IESBenchEval python=3.10
conda activate IESBenchEval
pip install -r requirements.txt
```






## 🗂 Dataset Format

IESBench was meticulously designed to challenge and evaluate image editing safety.
For more detailed information and accessing our dataset, please refer to our Huggingface page:

- The benchmark is available [here](https://huggingface.co/datasets)

- Every data is organized in json format as follows:

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
```
## ⚖️ LeaderBoard




## 📄 Citation

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

This dataset contains sensitive or harmful content that may be disturbing, This benchmark is provided for educational and research purposes only.




