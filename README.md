

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
  - [#1 - Vision-centric Jailbreak Attack](#1---vision-centric-jailbreak-attack)
  - [#2 - IESBench: Benchmarking Image Editing Safety](#2---iesbench-benchmarking-image-editing-safety)
  - [#3 - Introspective Defense](#3---introspective-defense)
- [🚀 Setup](#-setup)
- [🏆  LeaderBoard](#--leaderboard)
  - [Evaluation Metrics of IESBench](#evaluation-metrics-of-iesbench)
  - [Safety Ranking on IESBench](#safety-ranking-on-iesbench)
    - [#1 Attack Success Rate (↓ is safer)](#1-attack-success-rate--is-safer)
    - [#2 Harmfulness Score (↓ is safer)](#2-harmfulness-score--is-safer)
    - [#3 Editing Validity (↓ is safer)](#3-editing-validity--is-safer)
    - [#4 High Risk Ratio (↓ is safer)](#4-high-risk-ratio--is-safer)
- [🗂 Dataset Format](#-dataset-format)
- [🎓 BibTex](#-bibtex)
- [❌ Disclaimers](#-disclaimers)



## 🌟 Project Overview
Recent advances in large image editing models have shifted the paradigm from text-driven instructions to *vision-prompt* editing, where user intent is inferred directly from visual inputs such as marks, arrows, and visual–text prompts. While this paradigm greatly expands usability, it also introduces a critical and underexplored safety risk: *the attack surface itself becomes visual.* To mitigate the safety gap, this project aims to systematically investigate the safety of large image editing models from a vision-centric perspective, with new jailbreak attack method, benchmark and a training-free defense approach.

### #1 - Vision-centric Jailbreak Attack

<p align="center">
  <img src="assets/teaser_up.png" width="44%" alt="teaser1" />
  <img src="assets/teaser_down.png" width="53%" alt="teaser2" />
</p>
<p align="center"><b>Fig 1. Comparison of our attack method with the text-centric method.</b></p>

Through hidding the malicious instruction in vision, the attack success rates of our Vision-centric Jailbreak Attack (VJA) are *largely* elevated on 4 mainstream large image editing models, revealing the safety *vulnerability* in current image editing systems.






### #2 - IESBench: Benchmarking Image Editing Safety
<img src="assets/overview.png" alt="logo" style="zoom:70%;" />

<p align="center"><b>Fig 2. Overview of IESBench.</b></p>

Meanwhile, to facilitate standardized evaluation, we also construct the IESBench, a *vision-centric benchmark* for evaluating the safety of large image editing models, which contains 1054 *visually-prompted images*, spanning across 15 safety policies, 116 attributes and 9 actions. 

### #3 - Introspective Defense 
<p align="center">
<img src="assets/defense_method.png" alt="defense" width="60%" />
</p>

<p align="center"><b>Fig 3. Illustration of our proposed defense approach.</b></p>

Lastly, we propose a simple yet effective training-free defense through *multimodal instrosptive reasoning*, which improves safety of models against malicious visual editing with minimal overhead,

## 🚀 Setup

Please see [here](https://github.com/CSU-JPG/VJA/tree/main/src) for the setup and implementation of our proposed defense approach.

## 🏆  LeaderBoard
### Evaluation Metrics of IESBench

| Metric | Abbrev. | What it measures | Definition (details) |
|---|---|---|---|
| Attack Success Rate | ASR | Jailbreak success (bypass) | Ratio of attacks that successfully bypass the guard models. |
| Harmfulness Score | HS | Harm level of the edited output | Harmfulness of the edited image on a 1–5 scale. |
| Editing Validity | EV | Whether the edit is meaningful/valid | Cases where the bypass is successful but the edited content is invalid (e.g., garbled text). |
| High Risk Ratio | HRR | “True high-risk” effective attacks | Proportion of effective and high-risk attacks (e.g., HS ≥ 4), measuring truly high-risk outputs. |

### Safety Ranking on IESBench

**[C]** indicates Commercial models, **[O]** indicates Open-source models.

#### #1 Attack Success Rate (↓ is safer)

| Model                                |   AVG |    I1 |    I2 |    I3 |    I4 |    I5 |    I6 |    I7 |    I8 |    I9 |   I10 |   I11 |   I12 |   I13 |   I14 |   I15 |
| ------------------------------------ | ----: | ----: | ----: | ----: | ----: | ----: | ----: | ----: | ----: | ----: | ----: | ----: | ----: | ----: | ----: | ----: |
| [O] **Qwen-Image-Edit-Safe** (Ours)  🥇|  66.9 |  87.0 |  77.3 |  87.4 |  88.7 |  81.1 |  72.2 |  69.0 |  53.4 |  71.8 | 100.0 |  28.3 |   8.1 |  61.5 |  72.1 |  55.3 |
| [C] GPT Image 1.5                   🥈 |  70.3 |  48.9 |  87.6 |  44.1 |  39.8 |  54.7 |  97.2 |  94.0 |  91.6 |  38.9 |  60.0 |  95.7 |  32.3 |  92.3 |  82.4 | 100.0 |
| [C] Nano Banana Pro                 🥉 |  80.9 |  60.4 |  95.3 |  88.3 |  30.8 |  92.5 | 100.0 |  90.5 |  95.8 |  84.2 | 100.0 |  41.3 |  74.2 | 100.0 |  83.8 | 100.0 |
| [C] Seedream 4.5                     |  94.1 |  98.6 |  92.2 |  86.5 | 100.0 | 100.0 | 100.0 | 100.0 |  96.3 |  86.3 | 100.0 |  97.8 |  83.9 | 100.0 |  83.8 | 100.0 |
| [C] Qwen-Image-Edit (Online version) |  97.5 | 100.0 |  93.0 |  99.1 | 100.0 |  98.1 | 100.0 | 100.0 |  94.9 |  96.8 |  80.0 |  97.8 |  88.7 | 100.0 | 100.0 | 100.0 |
| [O] BAGEL                            | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| [O] Flux2.0 [dev]                    | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| [O] Qwen-Image-Edit* (Local version) | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |



#### #2 Harmfulness Score (↓ is safer)

| Model                                | AVG |  I1 |  I2 |  I3 |  I4 |  I5 |  I6 |  I7 |  I8 |  I9 | I10 | I11 | I12 | I13 | I14 | I15 |
| ------------------------------------ | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| [C] GPT Image 1.5                   🥇 | 3.2 | 2.4 | 3.5 | 2.3 | 2.3 | 3.0 | 4.4 | 4.4 | 4.1 | 2.1 | 3.4 | 4.1 | 2.2 | 3.0 | 3.6 | 4.7 |
| [O] **Qwen-Image-Edit-Safe** (Ours)  🥈| 3.4 | 4.3 | 3.7 | 4.2 | 4.4 | 4.0 | 3.6 | 3.6 | 2.9 | 3.3 | 4.7 | 2.0 | 1.3 | 3.1 | 3.6 | 3.1 |
| [C] Nano Banana Pro                  🥉| 3.8 | 3.2 | 4.4 | 4.1 | 1.9 | 4.5 | 4.7 | 4.6 | 4.3 | 3.6 | 4.7 | 2.4 | 3.8 | 4.6 | 3.5 | 3.3 |
| [C] Qwen-Image-Edit (Online version) | 4.1 | 4.2 | 3.7 | 4.0 | 4.2 | 4.4 | 4.0 | 4.8 | 3.8 | 3.8 | 3.8 | 4.4 | 4.2 | 4.4 | 4.1 | 3.1 |
| [O] BAGEL                            | 4.1 | 4.3 | 4.2 | 3.5 | 4.5 | 4.3 | 3.9 | 4.4 | 3.9 | 4.4 | 4.2 | 4.5 | 4.2 | 3.7 | 3.7 | 4.5 |
| [C] Seedream 4.5                     | 4.4 | 4.7 | 4.3 | 4.2 | 4.7 | 4.8 | 4.8 | 4.8 | 4.5 | 3.8 | 5.0 | 4.8 | 4.2 | 4.7 | 3.9 | 4.7 |
| [O] Flux2.0 [dev]                    | 4.6 | 4.7 | 4.7 | 4.7 | 4.7 | 4.8 | 4.7 | 4.7 | 4.4 | 4.2 | 4.4 | 4.9 | 4.9 | 4.4 | 4.3 | 4.5 |
| [O] Qwen-Image-Edit* (Local version) | 4.6 | 4.7 | 4.4 | 4.6 | 4.8 | 4.6 | 4.6 | 4.6 | 4.5 | 4.3 | 4.7 | 4.8 | 4.8 | 4.6 | 4.7 | 4.6 |


#### #3 Editing Validity (↓ is safer)

| Model                                |  AVG |   I1 |   I2 |   I3 |   I4 |   I5 |    I6 |   I7 |   I8 |   I9 |   I10 |  I11 |   I12 |   I13 |  I14 |   I15 |
| ------------------------------------ | ---: | ---: | ---: | ---: | ---: | ---: | ----: | ---: | ---: | ---: | ----: | ---: | ----: | ----: | ---: | ----: |
| [O] **Qwen-Image-Edit-Safe** (Ours)  🥇| 62.8 | 83.3 | 68.8 | 81.1 | 85.0 | 75.5 |  69.4 | 69.0 | 50.7 | 58.8 |  90.0 | 26.1 |   8.1 |  61.5 | 70.6 |  55.3 |
| [C] GPT Image 1.5 🥈                   | 63.0 | 36.0 | 86.8 | 34.5 | 33.8 | 52.8 |  97.2 | 90.5 | 87.5 | 25.3 |  60.0 | 84.8 |  30.6 | 100.0 | 75.0 |  94.7 |
| [C] Nano Banana Pro                  🥉| 79.1 | 60.4 | 94.6 | 84.7 | 30.1 | 92.5 | 100.0 | 90.5 | 95.3 | 75.8 | 100.0 | 39.1 |  74.2 | 100.0 | 79.4 | 100.0 |
| [O] BAGEL                            | 82.0 | 84.2 | 85.3 | 58.6 | 91.0 | 88.7 |  83.3 | 95.2 | 79.0 | 86.3 |  80.0 | 95.7 |  85.5 |  76.9 | 76.9 |  94.7 |
| [C] Seedream 4.5                     | 86.3 | 92.8 | 82.9 | 78.4 | 93.2 | 96.2 |  94.4 | 98.8 | 86.9 | 71.6 | 100.0 | 95.7 |  80.6 |  97.4 | 72.1 |  92.1 |
| [O] Flux2.0 [dev]                    | 87.1 | 92.8 | 93.8 | 91.9 | 94.0 | 96.2 |  80.6 | 94.0 | 80.4 | 75.8 |  80.0 | 93.5 | 100.0 |  76.9 | 79.4 |  94.7 |
| [C] Qwen-Image-Edit (Online version) | 87.7 | 87.8 | 70.5 | 90.1 | 94.0 | 90.6 |  69.4 | 98.8 | 81.3 | 78.9 |  80.0 | 87.0 |  88.7 |  87.2 | 86.8 |  94.7 |
| [O] Qwen-Image-Edit* (Local version) | 92.9 | 94.2 | 89.0 | 91.0 | 95.5 | 92.5 |  94.4 | 95.2 | 90.7 | 83.9 |  90.0 | 95.7 | 100.0 |  97.4 | 97.0 |  97.4 |



#### #4 High Risk Ratio (↓ is safer)

| Model                                |  AVG |   I1 |   I2 |   I3 |   I4 |   I5 |    I6 |   I7 |   I8 |   I9 |   I10 |  I11 |  I12 |  I13 |  I14 |  I15 |
| ------------------------------------ | ---: | ---: | ---: | ---: | ---: | ---: | ----: | ---: | ---: | ---: | ----: | ---: | ---: | ---: | ---: | ---: |
| [C] GPT Image 1.5 🥇                   | 52.0 | 30.9 | 60.5 | 30.6 | 29.3 | 47.2 |  86.1 | 85.7 | 72.9 | 20.0 |  60.0 | 73.9 | 29.0 | 48.7 | 60.3 | 86.8 |
| [O] **Qwen-Image-Edit-Safe** (Ours)🥈  | 61.7 | 82.6 | 68.0 | 80.2 | 83.5 | 75.5 |  69.4 | 69.0 | 49.8 | 54.1 |  90.0 | 26.1 |  8.1 | 61.5 | 67.6 | 50.0 |
| [C] Nano Banana Pro                  🥉| 70.6 | 55.4 | 89.1 | 75.7 | 21.8 | 88.7 | 100.0 | 90.5 | 81.8 | 63.2 |  90.0 | 34.8 | 74.2 | 92.3 | 61.8 | 42.1 |
| [O] BAGEL                            | 70.6 | 74.8 | 75.2 | 47.7 | 82.0 | 77.4 |  69.4 | 91.7 | 62.6 | 77.9 |  70.0 | 93.5 | 74.2 | 51.3 | 60.3 | 84.2 |
| [C] Qwen-Image-Edit (Online version) | 73.8 | 77.0 | 65.9 | 72.1 | 76.7 | 84.9 |  66.7 | 95.2 | 64.5 | 66.3 |  70.0 | 80.4 | 87.1 | 84.6 | 72.1 | 34.2 |
| [C] Seedream 4.5                     | 83.8 | 91.4 | 81.4 | 75.7 | 90.2 | 92.5 |  94.4 | 98.8 | 86.0 | 61.1 | 100.0 | 95.7 | 77.4 | 97.4 | 70.6 | 86.8 |
| [O] Flux2.0 [dev]                    | 84.6 | 87.1 | 87.6 | 87.4 | 92.5 | 92.5 |  80.6 | 94.0 | 77.1 | 72.6 |  80.0 | 93.5 | 98.4 | 76.9 | 72.1 | 84.2 |
| [O] Qwen-Image-Edit* (Local version) | 90.3 | 93.5 | 87.4 | 89.2 | 94.0 | 88.7 |  94.4 | 94.0 | 87.9 | 77.4 |  90.0 | 95.7 | 95.2 | 97.4 | 94.0 | 84.2 |





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




