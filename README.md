# Awesome-Efficient-LLM

A curated list for **Efficient Large Language Models**:
  - [Knowledge Distillation](knowledge_distillation.md)
  - [Network Pruning](pruning.md)
  - [Quantization](quantization.md)
  - [Inference Acceleration](inference_acceleration.md)
  - [Efficient MOE](efficient_moe.md)
  - [Efficient Architecture of LLM](efficient_architecture_llm.md)
  - [KV Cache Compression](kv_cache_compression.md)
  - [Text Compression](text_compression.md)
  - [Low-Rank Decomposition](low_rank_decomposition.md)
  - [Hardware/System](hardware.md)
  - [Tuning](tuning.md)
  - [Survey](survey.md)
  - [Leaderboard](leaderboard.md)

You can check out all the papers by selecting the sub-area you're interested in. On this page, we're showing papers released in the past 30 days.

#### 🚀 Updates
* May 29, 2023: We've had this awesome list for a year now :smiling_face_with_three_hearts:! But it's grown pretty long, so we're reorganizing it and would divide the list by their specific areas into different readme.
* Sep 27, 2023: Add tag ![Publish](https://img.shields.io/badge/Conference-NeurIPS'23-blue) for papers accepted at NeurIPS'23.
* Sep 6, 2023: Add a new subdirectory [project/](project/) to organize those projects that are designed for developing a lightweight LLM.
* July 11, 2023:
In light of the numerous publications that conducts experiments using PLMs (such as BERT, BART) currently, a new subdirectory [efficient_plm/](efficient_plm/) is created to house papers that are applicable to PLMs but have yet to be verified for their effectiveness on LLMs (not implying that they are not suitable on LLM). 


## Paper from 05/26/2024 - Now

| Title & Authors | Introduction | Links |
|:--|  :----: | :---:|
|Network Pruning | | |
|[FinerCut: Finer-grained Interpretable Layer Pruning for Large Language Models](https://arxiv.org/abs/2405.18218) <br> Yang Zhang, Yawei Li, Xinpeng Wang, Qianli Shen, Barbara Plank, Bernd Bischl, Mina Rezaei, Kenji Kawaguchi |<img width="1002" alt="image" src="https://arxiv.org/html/2405.18218v1/x1.png"> |[Paper](https://arxiv.org/abs/2405.18218)|  [//]: #05/29
|Quantization | | |
|[![Star](https://img.shields.io/github/stars/eth-sri/llm-quantization-attack.svg?style=social&label=Star)](https://github.com/eth-sri/llm-quantization-attack)<br>[Exploiting LLM Quantization](https://arxiv.org/abs/2405.18137) <br> Kazuki Egashira, Mark Vero, Robin Staab, Jingxuan He, Martin Vechev |<img width="1002" alt="image" src="figures/exploiting_llm_quantization.png"> |[Github](https://github.com/eth-sri/llm-quantization-attack) <br> [Paper](https://arxiv.org/abs/2405.18137)| [//]: #05/29
|[CLAQ: Pushing the Limits of Low-Bit Post-Training Quantization for LLMs](https://arxiv.org/abs/2405.17233) <br> Haoyu Wang, Bei Liu, Hang Shao, Bo Xiao, Ke Zeng, Guanglu Wan, Yanmin Qian |<img width="1002" alt="image" src="https://arxiv.org/html/2405.17233v1/x1.png"> |[Paper](https://arxiv.org/abs/2405.17233)| [//]: #05/29

#### 💮 Contributing

If you'd like to include your paper, or need to update any details such as conference information or code URLs, please feel free to submit a pull request. You can generate the required markdown format for each paper by filling in the information in `generate_item.py` and execute `python generate_item.py`. We warmly appreciate your contributions to this list. Alternatively, you can email me with the links to your paper and code, and I would add your paper to the list at my earliest convenience. 





