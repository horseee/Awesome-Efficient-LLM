# Awesome-Efficient-LLM
A curated list for **Efficient Large Language Models**

## Full List
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

### Please check out all the papers by selecting the sub-area you're interested in. On this page, we're showing papers released in the past 30 days.

#### 🚀 Updates
* May 29, 2023: We've had this awesome list for a year now :smiling_face_with_three_hearts:! It's grown pretty long, so we're reorganizing it and would divide the list by their specific areas into different readme.
* Sep 27, 2023: Add tag ![Publish](https://img.shields.io/badge/Conference-NeurIPS'23-blue) for papers accepted at NeurIPS'23.
* Sep 6, 2023: Add a new subdirectory [project/](project/) to organize those projects that are designed for developing a lightweight LLM.
* July 11, 2023:
In light of the numerous publications that conduct experiments using PLMs (such as BERT, BART) currently, a new subdirectory [efficient_plm/](efficient_plm/) is created to house papers that are applicable to PLMs but have yet to be verified for their effectiveness on LLMs (not implying that they are not suitable on LLM). 



## Paper from 05/26/2024 - Now ([Full List](#full-list))

| Title & Authors | Introduction | Links |
|:--|  :----: | :---:|
|**Network Pruning** | | |
|[FinerCut: Finer-grained Interpretable Layer Pruning for Large Language Models](https://arxiv.org/abs/2405.18218) <br> Yang Zhang, Yawei Li, Xinpeng Wang, Qianli Shen, Barbara Plank, Bernd Bischl, Mina Rezaei, Kenji Kawaguchi |<img width="1002" alt="image" src="https://arxiv.org/html/2405.18218v1/x1.png"> |[Paper](https://arxiv.org/abs/2405.18218)|  [//]: #05/29
|[![Star](https://img.shields.io/github/stars/Mohammad-Mozaffari/slope.svg?style=social&label=Star)](https://github.com/Mohammad-Mozaffari/slope)<br>[SLoPe: Double-Pruned Sparse Plus Lazy Low-Rank Adapter Pretraining of LLMs](https://arxiv.org/abs/2405.16325) <br> Mohammad Mozaffari, Amir Yazdanbakhsh, Zhao Zhang, Maryam Mehri Dehnavi |<img width="1002" alt="image" src="https://arxiv.org/html/2405.16325v1/x1.png"> |[Github](https://github.com/Mohammad-Mozaffari/slope) <br> [Paper](https://arxiv.org/abs/2405.16325)| [//]: #05/29
|[![Star](https://img.shields.io/github/stars/Lucky-Lance/SPP.svg?style=social&label=Star)](https://github.com/Lucky-Lance/SPP)<br>[SPP: Sparsity-Preserved Parameter-Efficient Fine-Tuning for Large Language Models](https://arxiv.org/abs/2405.16057) <br> Xudong Lu, Aojun Zhou, Yuhui Xu, Renrui Zhang, Peng Gao, Hongsheng Li |<img width="1002" alt="image" src="https://github.com/Lucky-Lance/SPP/raw/main/asserts/SPP.png"> |[Github](https://github.com/Lucky-Lance/SPP) <br> [Paper](https://arxiv.org/abs/2405.16057)| [//]: #05/29
|**Quantization** | | |
|[![Star](https://img.shields.io/github/stars/pilancilab/caldera.svg?style=social&label=Star)](https://github.com/pilancilab/caldera)<br>[Compressing Large Language Models using Low Rank and Low Precision Decomposition](https://arxiv.org/abs/2405.18886) <br> Rajarshi Saha, Naomi Sagan, Varun Srivastava, Andrea J. Goldsmith, Mert Pilanci |<img width="1002" alt="image" src="https://arxiv.org/html/2405.18886v1/x1.png"> |[Github](https://github.com/pilancilab/caldera) <br> [Paper](https://arxiv.org/abs/2405.18886)| [//]: #05/31
|[I-LLM: Efficient Integer-Only Inference for Fully-Quantized Low-Bit Large Language Models](https://arxiv.org/abs/2405.17849) <br> Xing Hu, Yuan Chen, Dawei Yang, Sifan Zhou, Zhihang Yuan, Jiangyong Yu, Chen Xu |<img width="1002" alt="image" src="figures/I-LLM.png"> |[Paper](https://arxiv.org/abs/2405.17849)| [//]: #05/29
|[![Star](https://img.shields.io/github/stars/eth-sri/llm-quantization-attack.svg?style=social&label=Star)](https://github.com/eth-sri/llm-quantization-attack)<br>[Exploiting LLM Quantization](https://arxiv.org/abs/2405.18137) <br> Kazuki Egashira, Mark Vero, Robin Staab, Jingxuan He, Martin Vechev |<img width="1002" alt="image" src="figures/exploiting_llm_quantization.png"> |[Github](https://github.com/eth-sri/llm-quantization-attack) <br> [Paper](https://arxiv.org/abs/2405.18137)| [//]: #05/29
|[CLAQ: Pushing the Limits of Low-Bit Post-Training Quantization for LLMs](https://arxiv.org/abs/2405.17233) <br> Haoyu Wang, Bei Liu, Hang Shao, Bo Xiao, Ke Zeng, Guanglu Wan, Yanmin Qian |<img width="1002" alt="image" src="https://arxiv.org/html/2405.17233v1/x1.png"> |[Paper](https://arxiv.org/abs/2405.17233)| [//]: #05/29
|[SpinQuant -- LLM quantization with learned rotations](https://arxiv.org/abs/2405.16406) <br> Zechun Liu, Changsheng Zhao, Igor Fedorov, Bilge Soran, Dhruv Choudhary, Raghuraman Krishnamoorthi, Vikas Chandra, Yuandong Tian, Tijmen Blankevoort |<img width="1002" alt="image" src="figures/spinquant.png"> |[Paper](https://arxiv.org/abs/2405.16406)| [//]: #05/29
|[![Star](https://img.shields.io/github/stars/Aaronhuang-778/SliM-LLM.svg?style=social&label=Star)](https://github.com/Aaronhuang-778/SliM-LLM)<br>[SliM-LLM: Salience-Driven Mixed-Precision Quantization for Large Language Models](https://arxiv.org/abs/2405.14917) <br> Wei Huang, Haotong Qin, Yangdong Liu, Yawei Li, Xianglong Liu, Luca Benini, Michele Magno, Xiaojuan Qi |<img width="1002" alt="image" src="https://github.com/Aaronhuang-778/SliM-LLM/blob/main/imgs/WX20240527-155305@2x.png"> |[Github](https://github.com/Aaronhuang-778/SliM-LLM) <br> [Paper](https://arxiv.org/abs/2405.14917)| [//]: #05/29
|[![Star](https://img.shields.io/github/stars/tree/pv-tuning.svg?style=social&label=Star)](https://github.com/tree/pv-tuning)<br>[PV-Tuning: Beyond Straight-Through Estimation for Extreme LLM Compression](https://arxiv.org/abs/2405.14852) <br> Vladimir Malinovskii, Denis Mazur, Ivan Ilin, Denis Kuznedelev, Konstantin Burlachenko, Kai Yi, Dan Alistarh, Peter Richtarik |<img width="1002" alt="image" src="figures/pv-tuning.png"> |[Github](https://github.com/Vahe1994/AQLM/tree/pv-tuning) <br> [Paper](https://arxiv.org/abs/2405.14852)| [//]: #05/29
|[Integer Scale: A Free Lunch for Faster Fine-grained Quantization of LLMs](https://arxiv.org/abs/2405.14597) <br> Qingyuan Li, Ran Meng, Yiduo Li, Bo Zhang, Yifan Lu, Yerui Sun, Lin Ma, Yuchen Xie |<img width="1002" alt="image" src="https://arxiv.org/html/2405.14597v2/x2.png"> |[Paper](https://arxiv.org/abs/2405.14597)|  [//]: #05/29
|**Inference Acceleration** | | |
|[Faster Cascades via Speculative Decoding](https://arxiv.org/abs/2405.19261) <br> Harikrishna Narasimhan, Wittawat Jitkrittum, Ankit Singh Rawat, Seungyeon Kim, Neha Gupta, Aditya Krishna Menon, Sanjiv Kumar |<img width="1002" alt="image" src="figures/speccascade.png"> |[Paper](https://arxiv.org/abs/2405.19261)| [//]: #05/31
|[![Star](https://img.shields.io/github/stars/hmarkc/parallel-prompt-decoding.svg?style=social&label=Star)](https://github.com/hmarkc/parallel-prompt-decoding)<br>[Hardware-Aware Parallel Prompt Decoding for Memory-Efficient Acceleration of LLM Inference](https://arxiv.org/abs/2405.18628) <br> Hao (Mark)Chen, Wayne Luk, Ka Fai Cedric Yiu, Rui Li, Konstantin Mishchenko, Stylianos I. Venieris, Hongxiang Fan |<img width="1002" alt="image" src="https://github.com/hmarkc/parallel-prompt-decoding/raw/main/assets/Overview.png"> |[Github](https://github.com/hmarkc/parallel-prompt-decoding) <br> [Paper](https://arxiv.org/abs/2405.18628)| [//]: #05/31
|**Efficient MOE** | | |
|[![Publish](https://img.shields.io/badge/Conference-DAC'24-blue)]()<br>[MoNDE: Mixture of Near-Data Experts for Large-Scale Sparse Models](https://arxiv.org/abs/2405.18832) <br> Taehyun Kim, Kwanseok Choi, Youngmock Cho, Jaehoon Cho, Hyuk-Jae Lee, Jaewoong Sim |<img width="1002" alt="image" src="https://arxiv.org/html/2405.18832v1/x4.png"> |[Paper](https://arxiv.org/abs/2405.18832)| [//]: #05/31
|[![Star](https://img.shields.io/github/stars/LINs-lab/DynMoE.svg?style=social&label=Star)](https://github.com/LINs-lab/DynMoE)<br>[Dynamic Mixture of Experts: An Auto-Tuning Approach for Efficient Transformer Models](https://arxiv.org/abs/2405.14297) <br> Yongxin Guo, Zhenglin Cheng, Xiaoying Tang, Tao Lin |<img width="1002" alt="image" src="figures/dynmoe.png"> |[Github](https://github.com/LINs-lab/DynMoE) <br> [Paper](https://arxiv.org/abs/2405.14297)| [//]: #05/29
|[![Publish](https://img.shields.io/badge/Conference-ICML'24-blue)]()<br>[A Provably Effective Method for Pruning Experts in Fine-tuned Sparse Mixture-of-Experts](https://arxiv.org/pdf/2405.16646) <br> Mohammed Nowaz Rabbani Chowdhury, Meng Wang, Kaoutar El Maghraoui, Naigang Wang, Pin-Yu Chen, Christopher Carothers |<img width="1002" alt="image" src="https://arxiv.org/html/2405.16646v2/extracted/5626402/Fig/token_expert_combined_2.png"> |[Paper](https://arxiv.org/pdf/2405.16646)| [//]: #05/29
|**KV Cache Compression** | | |
|[ZipCache: Accurate and Efficient KV Cache Quantization with Salient Token Identification](https://arxiv.org/abs/2405.14256) <br> Yefei He, Luoming Zhang, Weijia Wu, Jing Liu, Hong Zhou, Bohan Zhuang |<img width="1002" alt="image" src="figures/zipcache.png"> |[Paper](https://arxiv.org/abs/2405.14256)| [//]: #05/29
|**Hardware/System** | | |
|[![Publish](https://img.shields.io/badge/Conference-OSDI'24-blue)]()<br>[Parrot: Efficient Serving of LLM-based Applications with Semantic Variable](https://arxiv.org/abs/2405.19888) <br> Chaofan Lin, Zhenhua Han, Chengruidong Zhang, Yuqing Yang, Fan Yang, Chen Chen, Lili Qiu |<img width="1002" alt="image" src="figures/parrot.png"> |[Paper](https://arxiv.org/abs/2405.19888)| [//]: #05/31
 
#### 💮 Contributing

If you'd like to include your paper, or need to update any details such as conference information or code URLs, please feel free to submit a pull request. You can generate the required markdown format for each paper by filling in the information in `generate_item.py` and execute `python generate_item.py`. We warmly appreciate your contributions to this list. Alternatively, you can email me with the links to your paper and code, and I would add your paper to the list at my earliest convenience. 





