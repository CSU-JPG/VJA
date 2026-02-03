##  When the Prompt Becomes Visual: Vision-Centric Jailbreak Attacks for Large Image Editing Models
[**🌐 GitHub**]() | [**🛎 Project Page**]() ｜ [**👉 Download full datasets**]()

<p align="center">
  <img src="assets/logo.png" alt="logo" width="200"/>
</p>


---

## 📢 Updates

- **[2026-1-1]**: Released IESBench version 1.0 🔥


## 🌟 About IESBench
IESBench, the first standardized benchmark for evaluating image editing safety, enabling principled analysis of vision-centric jailbreak attacks.

<img src="assets/overview.png" alt="logo" style="zoom:70%;" />

<p align="center"><b>Overview of IESBench.</b></p>

IESBench contains 1054 attack images, across 15 safety policies, 116 attributes and 9 actions. 

---

## 📑 Table of Contents
- [Setup](#️-setup)
- [Accessing Datasets](#-accessing-datasets)
- [Data Format](#-data-format)
- [Evaluation](#-evaluation)
- [Update](#-update)
- [Citation](#-citation)
- [Disclaimers](#-disclaimers)
- [Contact](#-contact)

---

## 🚀 Setup

To set up the environment for evaluation:

```bash
conda create -n IESBenchEval python=3.10
conda activate IESBenchEval
pip install -r requirements.txt
```

---

## 📂 Accessing Datasets

IESBench was meticulously designed to challenge and evaluate image editing safety.
For more detailed information and accessing our dataset, please refer to our Huggingface page:

- 🧑‍🔬 [IESBench](https://huggingface.co/datasets)
- 
---

## 🗂 Dataset Format

- The dataset is provided in jsonl format and contains the following attributes:

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

---


## ⚖️ Evaluation

Please refer to our evaluation folders for detailed information on evaluating with the ISEBench:

- 🔍 [IESBench Evaluation](https://github.com)

---

## 📄 Citation

If you find our work useful, please cite us:

```bibtex
@misc{ 
}
```

---

## ❌ Disclaimers
This dataset contains sensitive or harmful content that may be disturbing, This benchmark is provided for educational and research purposes only.

---


## ☎️ Contact

For questions, suggestions or issues, feel free to open an [issue](https://github.com) on GitHub.

---
