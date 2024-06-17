# Awesome-Efficient-LLM
A curated list for **Efficient Large Language Models**

## Full List
  - [Knowledge Distillation](knowledge_distillation.md)
  - [Network Pruning / Sparsity](pruning.md)
  - [Quantization](quantization.md)
  - [Inference Acceleration](inference_acceleration.md)
  - [Efficient MOE](efficient_moe.md)
  - [Efficient Architecture of LLM](efficient_architecture_llm.md)
  - [KV Cache Compression](kv_cache_compression.md)
  - [Text Compression](text_compression.md)
  - [Low-Rank Decomposition](low_rank_decomposition.md)
  - [Hardware / System](hardware.md)
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



## Paper from 05/26/2024 - Now (see Full List from 05/22/2023 [here](#full-list))

#### Knowledge Distillation

| Title & Authors | Introduction | Links |
|:--|  :----: | :---:|
|[LLM and GNN are Complementary: Distilling LLM for Multimodal Graph Learning](https://arxiv.org/abs/2406.01032) <br> Junjie Xu, Zongyu Wu, Minhua Lin, Xiang Zhang, Suhang Wang |<img width="1002" alt="image" src="https://arxiv.org/html/2406.01032v1/x1.png"> |[Paper](https://arxiv.org/abs/2406.01032)|[//]: #06/05
|[![Star](https://img.shields.io/github/stars/jiachenwestlake/MMKD.svg?style=social&label=Star)](https://github.com/jiachenwestlake/MMKD)<br>[Adversarial Moment-Matching Distillation of Large Language Models](https://arxiv.org/abs/2406.02959) <br> Chen Jia |<img width="1002" alt="image" src="https://arxiv.org/html/2406.02959v1/x1.png"> |[Github](https://github.com/jiachenwestlake/MMKD) <br> [Paper](https://arxiv.org/abs/2406.02959)|[//]: #06/11

#### Network Pruning / Sparsity
| Title & Authors | Introduction | Links |
|:--|  :----: | :---:|
|[![Star](https://img.shields.io/github/stars/ShiningSord/MoreauPruner.svg?style=social&label=Star)](https://github.com/ShiningSord/MoreauPruner)<br>[MoreauPruner: Robust Pruning of Large Language Models against Weight Perturbations](https://arxiv.org/abs/2406.07017) <br> Zixiao Wang, Jingwei Zhang, Wenqian Zhao, Farzan Farnia, Bei Yu |<img width="1002" alt="image" src="https://arxiv.org/html/2406.07017v1/x1.png"> |[Github](https://github.com/ShiningSord/MoreauPruner) <br> [Paper](https://arxiv.org/abs/2406.07017)|[//]: #06/12
|[![Star](https://img.shields.io/github/stars/pprp/Pruner-Zero.svg?style=social&label=Star)](https://github.com/pprp/Pruner-Zero)[![Publish](https://img.shields.io/badge/Conference-ICML'24-blue)]()<br>[Pruner-Zero: Evolving Symbolic Pruning Metric from scratch for Large Language Models](https://arxiv.org/abs/2406.02924) <br> Peijie Dong, Lujun Li, Zhenheng Tang, Xiang Liu, Xinglin Pan, Qiang Wang, Xiaowen Chu |<img width="1002" alt="image" src="https://raw.githubusercontent.com/pprp/Pruner-Zero/main/.github/images/pruner-zero-main-figure.png"> |[Github](https://github.com/pprp/Pruner-Zero) <br> [Paper](https://arxiv.org/abs/2406.02924)|[//]: #06/11
|[Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters](https://arxiv.org/abs/2406.05955) <br> Yixin Song, Haotong Xie, Zhengyan Zhang, Bo Wen, Li Ma, Zeyu Mi, Haibo Chen |<img width="1002" alt="image" src="https://arxiv.org/html/2406.05955v1/x2.png"> |[Paper](https://arxiv.org/abs/2406.05955) <br> [Model](https://huggingface.co/PowerInfer/TurboSparse-Mixtral) |[//]: #06/11
|[VTrans: Accelerating Transformer Compression with Variational Information Bottleneck based Pruning](https://arxiv.org/abs/2406.05276) <br> Oshin Dutta, Ritvik Gupta, Sumeet Agarwal |<img width="1002" alt="image" src="figures/VTrans.png"> |[Paper](https://arxiv.org/abs/2406.05276)|[//]: #06/11
|[![Type](https://img.shields.io/badge/w/Quantization-39B0A9)]() [Effective Interplay between Sparsity and Quantization: From Theory to Practice](https://arxiv.org/abs/2405.20935) <br> Simla Burcu Harma, Ayan Chakraborty, Elizaveta Kostenok, Danila Mishin, Dongho Ha, Babak Falsafi, Martin Jaggi, Ming Liu, Yunho Oh, Suvinay Subramanian, Amir Yazdanbakhsh ||[Paper](https://arxiv.org/abs/2405.20935)|[//]: #06/05
|[Large Language Model Pruning](https://arxiv.org/abs/2406.00030) <br> Hanjuan Huang, Hao-Jia Song, Hsing-Kuo Pao |<img width="1002" alt="image" src="https://arxiv.org/html/2406.00030v1/x1.png"> |[Paper](https://arxiv.org/abs/2406.00030)|[//]: #06/05
|[FinerCut: Finer-grained Interpretable Layer Pruning for Large Language Models](https://arxiv.org/abs/2405.18218) <br> Yang Zhang, Yawei Li, Xinpeng Wang, Qianli Shen, Barbara Plank, Bernd Bischl, Mina Rezaei, Kenji Kawaguchi |<img width="1002" alt="image" src="https://arxiv.org/html/2405.18218v1/x1.png"> |[Paper](https://arxiv.org/abs/2405.18218)|  [//]: #05/29
|[![Star](https://img.shields.io/github/stars/Mohammad-Mozaffari/slope.svg?style=social&label=Star)](https://github.com/Mohammad-Mozaffari/slope)<br>[SLoPe: Double-Pruned Sparse Plus Lazy Low-Rank Adapter Pretraining of LLMs](https://arxiv.org/abs/2405.16325) <br> Mohammad Mozaffari, Amir Yazdanbakhsh, Zhao Zhang, Maryam Mehri Dehnavi |<img width="1002" alt="image" src="https://arxiv.org/html/2405.16325v1/x1.png"> |[Github](https://github.com/Mohammad-Mozaffari/slope) <br> [Paper](https://arxiv.org/abs/2405.16325)| [//]: #05/29
|[![Star](https://img.shields.io/github/stars/Lucky-Lance/SPP.svg?style=social&label=Star)](https://github.com/Lucky-Lance/SPP)<br>[SPP: Sparsity-Preserved Parameter-Efficient Fine-Tuning for Large Language Models](https://arxiv.org/abs/2405.16057) <br> Xudong Lu, Aojun Zhou, Yuhui Xu, Renrui Zhang, Peng Gao, Hongsheng Li |<img width="1002" alt="image" src="https://github.com/Lucky-Lance/SPP/raw/main/asserts/SPP.png"> |[Github](https://github.com/Lucky-Lance/SPP) <br> [Paper](https://arxiv.org/abs/2405.16057)| [//]: #05/29

#### Quantization
| Title & Authors | Introduction | Links |
|:--|  :----: | :---:|
|[![Star](https://img.shields.io/github/stars/HandH1998/QQQ.svg?style=social&label=Star)](https://github.com/HandH1998/QQQ)<br>[QQQ: Quality Quattuor-Bit Quantization for Large Language Models](https://arxiv.org/abs/2406.09904) <br> Ying Zhang, Peng Zhang, Mincong Huang, Jingyang Xiang, Yujie Wang, Chao Wang, Yineng Zhang, Lei Yu, Chuan Liu, Wei Lin |<img width="202" alt="image" src="https://arxiv.org/html/2406.09904v1/x1.png"> |[Github](https://github.com/HandH1998/QQQ) <br> [Paper](https://arxiv.org/abs/2406.09904)|[//]: #06/18
|[![Star](https://img.shields.io/github/stars/GATECH-EIC/ShiftAddLLM.svg?style=social&label=Star)](https://github.com/GATECH-EIC/ShiftAddLLM)<br>[ShiftAddLLM: Accelerating Pretrained LLMs via Post-Training Multiplication-Less Reparameterization](https://arxiv.org/abs/2406.05981) <br> Haoran You, Yipin Guo, Yichao Fu, Wei Zhou, Huihong Shi, Xiaofan Zhang, Souvik Kundu, Amir Yazdanbakhsh, Yingyan Lin |<img width="1002" alt="image" src="https://github.com/GATECH-EIC/ShiftAddLLM/raw/main/assets/overview.jpg"> |[Github](https://github.com/GATECH-EIC/ShiftAddLLM) <br> [Paper](https://arxiv.org/abs/2406.05981)|[//]: #06/11
|[Low-Rank Quantization-Aware Training for LLMs](https://arxiv.org/abs/2406.06385) <br> Yelysei Bondarenko, Riccardo Del Chiaro, Markus Nagel |<img width="1002" alt="image" src="https://arxiv.org/html/2406.06385v1/extracted/5656645/img/01_lora_qat_proposed_palette.png"> |[Paper](https://arxiv.org/abs/2406.06385)|[//]: #06/11
|[LCQ: Low-Rank Codebook based Quantization for Large Language Models](https://arxiv.org/abs/2405.20973) <br> Wen-Pu Cai, Wu-Jun Li |<img width="1002" alt="image" src="https://arxiv.org/html/2405.20973v1/x5.png"> |[Paper](https://arxiv.org/abs/2405.20973)|[//]: #06/05
|[MagR: Weight Magnitude Reduction for Enhancing Post-Training Quantization](https://arxiv.org/abs/2406.00800) <br> Aozhong Zhang, Naigang Wang, Yanxia Deng, Xin Li, Zi Yang, Penghang Yin |<img width="1002" alt="image" src="https://arxiv.org/html/2406.00800v1/extracted/5638265/figure/magr.png"> |[Paper](https://arxiv.org/abs/2406.00800)|[//]: #06/05
|[Outliers and Calibration Sets have Diminishing Effect on Quantization of Modern LLMs](https://arxiv.org/abs/2405.20835) <br> Davide Paglieri, Saurabh Dash, Tim Rocktäschel, Jack Parker-Holder | |[Paper](https://arxiv.org/abs/2405.20835)|[//]: #06/05
|[![Star](https://img.shields.io/github/stars/pilancilab/caldera.svg?style=social&label=Star)](https://github.com/pilancilab/caldera)<br>[Compressing Large Language Models using Low Rank and Low Precision Decomposition](https://arxiv.org/abs/2405.18886) <br> Rajarshi Saha, Naomi Sagan, Varun Srivastava, Andrea J. Goldsmith, Mert Pilanci |<img width="1002" alt="image" src="https://arxiv.org/html/2405.18886v1/x1.png"> |[Github](https://github.com/pilancilab/caldera) <br> [Paper](https://arxiv.org/abs/2405.18886)| [//]: #05/31
|[I-LLM: Efficient Integer-Only Inference for Fully-Quantized Low-Bit Large Language Models](https://arxiv.org/abs/2405.17849) <br> Xing Hu, Yuan Chen, Dawei Yang, Sifan Zhou, Zhihang Yuan, Jiangyong Yu, Chen Xu |<img width="1002" alt="image" src="figures/I-LLM.png"> |[Paper](https://arxiv.org/abs/2405.17849)| [//]: #05/29
|[![Star](https://img.shields.io/github/stars/eth-sri/llm-quantization-attack.svg?style=social&label=Star)](https://github.com/eth-sri/llm-quantization-attack)<br>[Exploiting LLM Quantization](https://arxiv.org/abs/2405.18137) <br> Kazuki Egashira, Mark Vero, Robin Staab, Jingxuan He, Martin Vechev |<img width="1002" alt="image" src="figures/exploiting_llm_quantization.png"> |[Github](https://github.com/eth-sri/llm-quantization-attack) <br> [Paper](https://arxiv.org/abs/2405.18137)| [//]: #05/29
|[CLAQ: Pushing the Limits of Low-Bit Post-Training Quantization for LLMs](https://arxiv.org/abs/2405.17233) <br> Haoyu Wang, Bei Liu, Hang Shao, Bo Xiao, Ke Zeng, Guanglu Wan, Yanmin Qian |<img width="1002" alt="image" src="https://arxiv.org/html/2405.17233v1/x1.png"> |[Paper](https://arxiv.org/abs/2405.17233)| [//]: #05/29
|[SpinQuant -- LLM quantization with learned rotations](https://arxiv.org/abs/2405.16406) <br> Zechun Liu, Changsheng Zhao, Igor Fedorov, Bilge Soran, Dhruv Choudhary, Raghuraman Krishnamoorthi, Vikas Chandra, Yuandong Tian, Tijmen Blankevoort |<img width="1002" alt="image" src="figures/spinquant.png"> |[Paper](https://arxiv.org/abs/2405.16406)| [//]: #05/29
|[![Star](https://img.shields.io/github/stars/Aaronhuang-778/SliM-LLM.svg?style=social&label=Star)](https://github.com/Aaronhuang-778/SliM-LLM)<br>[SliM-LLM: Salience-Driven Mixed-Precision Quantization for Large Language Models](https://arxiv.org/abs/2405.14917) <br> Wei Huang, Haotong Qin, Yangdong Liu, Yawei Li, Xianglong Liu, Luca Benini, Michele Magno, Xiaojuan Qi |<img width="1002" alt="image" src="https://github.com/Aaronhuang-778/SliM-LLM/blob/main/imgs/WX20240527-155305@2x.png"> |[Github](https://github.com/Aaronhuang-778/SliM-LLM) <br> [Paper](https://arxiv.org/abs/2405.14917)| [//]: #05/29
|[![Star](https://img.shields.io/github/stars/tree/pv-tuning.svg?style=social&label=Star)](https://github.com/tree/pv-tuning)<br>[PV-Tuning: Beyond Straight-Through Estimation for Extreme LLM Compression](https://arxiv.org/abs/2405.14852) <br> Vladimir Malinovskii, Denis Mazur, Ivan Ilin, Denis Kuznedelev, Konstantin Burlachenko, Kai Yi, Dan Alistarh, Peter Richtarik |<img width="1002" alt="image" src="figures/pv-tuning.png"> |[Github](https://github.com/Vahe1994/AQLM/tree/pv-tuning) <br> [Paper](https://arxiv.org/abs/2405.14852)| [//]: #05/29
|[Integer Scale: A Free Lunch for Faster Fine-grained Quantization of LLMs](https://arxiv.org/abs/2405.14597) <br> Qingyuan Li, Ran Meng, Yiduo Li, Bo Zhang, Yifan Lu, Yerui Sun, Lin Ma, Yuchen Xie |<img width="1002" alt="image" src="https://arxiv.org/html/2405.14597v2/x2.png"> |[Paper](https://arxiv.org/abs/2405.14597)|  [//]: #05/29

#### Inference Acceleration
| Title & Authors | Introduction | Links |
|:--|  :----: | :---:|
|[HiP Attention: Sparse Sub-Quadratic Attention with Hierarchical Attention Pruning](https://arxiv.org/abs/2406.09827) <br> Heejun Lee, Geon Park, Youngwan Lee, Jina Kim, Wonyoung Jeong, Myeongjae Jeon, Sung Ju Hwang |<img width="1002" alt="image" src="https://arxiv.org/html/2406.09827v1/x1.png"> |[Paper](https://arxiv.org/abs/2406.09827)|[//]: #06/18
|[![Star](https://img.shields.io/github/stars/GATECH-EIC/Linearized-LLM.svg?style=social&label=Star)](https://github.com/GATECH-EIC/Linearized-LLM)[![Publish](https://img.shields.io/badge/Conference-ICML'24-blue)]()<br>[When Linear Attention Meets Autoregressive Decoding: Towards More Effective and Efficient Linearized Large Language Models](https://arxiv.org/abs/2406.07368) <br> Haoran You, Yichao Fu, Zheng Wang, Amir Yazdanbakhsh, Yingyan (Celine)Lin |<img width="1002" alt="image" src="https://arxiv.org/html/2406.07368v1/x5.png"> |[Github](https://github.com/GATECH-EIC/Linearized-LLM) <br> [Paper](https://arxiv.org/abs/2406.07368)|[//]: #06/12
|[![Star](https://img.shields.io/github/stars/dvlab-research/Q-LLM.svg?style=social&label=Star)](https://github.com/dvlab-research/Q-LLM)<br>[QuickLLaMA: Query-aware Inference Acceleration for Large Language Models](https://arxiv.org/abs/2406.07528) <br> Jingyao Li, Han Shi, Xin Jiang, Zhenguo Li, Hong Xu, Jiaya Jia |<img width="1002" alt="image" src="https://github.com/dvlab-research/Q-LLM/raw/master/img/framework.png"> |[Github](https://github.com/dvlab-research/Q-LLM) <br> [Paper](https://arxiv.org/abs/2406.07528)|[//]: #06/12
|[![Publish](https://img.shields.io/badge/Conference-ACL'24%20Findings-blue)]()<br>[Speculative Decoding via Early-exiting for Faster LLM Inference with Thompson Sampling Control Mechanism](https://arxiv.org/abs/2406.03853) <br> Jiahao Liu, Qifan Wang, Jingang Wang, Xunliang Cai |<img width="1002" alt="image" src="https://arxiv.org/html/2406.03853v1/x3.png"> |[Paper](https://arxiv.org/abs/2406.03853)|[//]: #06/12
|[Faster Cascades via Speculative Decoding](https://arxiv.org/abs/2405.19261) <br> Harikrishna Narasimhan, Wittawat Jitkrittum, Ankit Singh Rawat, Seungyeon Kim, Neha Gupta, Aditya Krishna Menon, Sanjiv Kumar |<img width="1002" alt="image" src="figures/speccascade.png"> |[Paper](https://arxiv.org/abs/2405.19261)| [//]: #05/31
|[![Star](https://img.shields.io/github/stars/hmarkc/parallel-prompt-decoding.svg?style=social&label=Star)](https://github.com/hmarkc/parallel-prompt-decoding)<br>[Hardware-Aware Parallel Prompt Decoding for Memory-Efficient Acceleration of LLM Inference](https://arxiv.org/abs/2405.18628) <br> Hao (Mark)Chen, Wayne Luk, Ka Fai Cedric Yiu, Rui Li, Konstantin Mishchenko, Stylianos I. Venieris, Hongxiang Fan |<img width="1002" alt="image" src="https://github.com/hmarkc/parallel-prompt-decoding/raw/main/assets/Overview.png"> |[Github](https://github.com/hmarkc/parallel-prompt-decoding) <br> [Paper](https://arxiv.org/abs/2405.18628)| [//]: #05/31

#### Efficient MOE
| Title & Authors | Introduction | Links |
|:--|  :----: | :---:|
|[![Star](https://img.shields.io/github/stars/UNITES-Lab/moe-quantization.svg?style=social&label=Star)](https://github.com/UNITES-Lab/moe-quantization)<br>[Examining Post-Training Quantization for Mixture-of-Experts: A Benchmark](https://arxiv.org/abs/2406.08155) <br> Pingzhi Li, Xiaolong Jin, Yu Cheng, Tianlong Chen |<img width="1002" alt="image" src="https://arxiv.org/html/2406.08155v1/x1.png"> |[Github](https://github.com/UNITES-Lab/moe-quantization) <br> [Paper](https://arxiv.org/abs/2406.08155)|[//]: #06/18
|[ME-Switch: A Memory-Efficient Expert Switching Framework for Large Language Models](https://arxiv.org/abs/2406.09041) <br> Jing Liu, Ruihao Gong, Mingyang Zhang, Yefei He, Jianfei Cai, Bohan Zhuang |<img width="1002" alt="image" src="https://arxiv.org/html/2406.09041v1/x1.png"> |[Paper](https://arxiv.org/abs/2406.09041)|[//]: #06/18
|[Demystifying the Compression of Mixture-of-Experts Through a Unified Framework](https://arxiv.org/abs/2406.02500) <br> Shwai He, Daize Dong, Liang Ding, Ang Li |<img width="1002" alt="image" src="https://arxiv.org/html/2406.02500v1/x1.png"> |[Paper](https://arxiv.org/abs/2406.02500)| [//]: #06/05
|[![Publish](https://img.shields.io/badge/Conference-DAC'24-blue)]()<br>[MoNDE: Mixture of Near-Data Experts for Large-Scale Sparse Models](https://arxiv.org/abs/2405.18832) <br> Taehyun Kim, Kwanseok Choi, Youngmock Cho, Jaehoon Cho, Hyuk-Jae Lee, Jaewoong Sim |<img width="1002" alt="image" src="https://arxiv.org/html/2405.18832v1/x4.png"> |[Paper](https://arxiv.org/abs/2405.18832)| [//]: #05/31
|[![Star](https://img.shields.io/github/stars/LINs-lab/DynMoE.svg?style=social&label=Star)](https://github.com/LINs-lab/DynMoE)<br>[Dynamic Mixture of Experts: An Auto-Tuning Approach for Efficient Transformer Models](https://arxiv.org/abs/2405.14297) <br> Yongxin Guo, Zhenglin Cheng, Xiaoying Tang, Tao Lin |<img width="1002" alt="image" src="figures/dynmoe.png"> |[Github](https://github.com/LINs-lab/DynMoE) <br> [Paper](https://arxiv.org/abs/2405.14297)| [//]: #05/29
|[![Publish](https://img.shields.io/badge/Conference-ICML'24-blue)]()<br>[A Provably Effective Method for Pruning Experts in Fine-tuned Sparse Mixture-of-Experts](https://arxiv.org/pdf/2405.16646) <br> Mohammed Nowaz Rabbani Chowdhury, Meng Wang, Kaoutar El Maghraoui, Naigang Wang, Pin-Yu Chen, Christopher Carothers |<img width="1002" alt="image" src="https://arxiv.org/html/2405.16646v2/extracted/5626402/Fig/token_expert_combined_2.png"> |[Paper](https://arxiv.org/pdf/2405.16646)| [//]: #05/29

#### Efficient Architecture of LLM
|[![Star](https://img.shields.io/github/stars/itsnamgyu/block-transformer.svg?style=social&label=Star)](https://github.com/itsnamgyu/block-transformer)<br>[Block Transformer: Global-to-Local Language Modeling for Fast Inference](https://arxiv.org/abs/2406.02657) <br> Namgyu Ho, Sangmin Bae, Taehyeon Kim, Hyunjik Jo, Yireun Kim, Tal Schuster, Adam Fisch, James Thorne, Se-Young Yun |<img width="1002" alt="image" src="https://arxiv.org/html/2406.02657v1/x1.png"> |[Github](https://github.com/itsnamgyu/block-transformer) <br> [Paper](https://arxiv.org/abs/2406.02657)|[//]: #06/12

#### KV Cache Compression
| Title & Authors | Introduction | Links |
|:--|  :----: | :---:|
|[![Star](https://img.shields.io/github/stars/zaydzuhri/pythia-mlkv.svg?style=social&label=Star)](https://github.com/zaydzuhri/pythia-mlkv)<br>[MLKV: Multi-Layer Key-Value Heads for Memory Efficient Transformer Decoding](https://arxiv.org/abs/2406.09297) <br> Zayd Muhammad Kawakibi Zuhri, Muhammad Farid Adilazuarda, Ayu Purwarianti, Alham Fikri Aji |<img width="1002" alt="image" src="https://arxiv.org/html/2406.09297v1/extracted/5665367/resources/mlkv-All_KV.png"> |[Github](https://github.com/zaydzuhri/pythia-mlkv) <br> [Paper](https://arxiv.org/abs/2406.09297)|[//]: #06/18
|[Loki: Low-Rank Keys for Efficient Sparse Attention](https://arxiv.org/abs/2406.02542) <br> Prajwal Singhania, Siddharth Singh, Shwai He, Soheil Feizi, Abhinav Bhatele |<img width="1002" alt="image" src="https://arxiv.org/html/2406.02542v1/x2.png"> |[Paper](https://arxiv.org/abs/2406.02542)|[//]: #06/12
|[![Star](https://img.shields.io/github/stars/amirzandieh/QJL.svg?style=social&label=Star)](https://github.com/amirzandieh/QJL)<br>[QJL: 1-Bit Quantized JL Transform for KV Cache Quantization with Zero Overhead](https://arxiv.org/abs/2406.03482) <br> Amir Zandieh, Majid Daliri, Insu Han |<img width="1002" alt="image" src="figures/QJL.png"> |[Github](https://github.com/amirzandieh/QJL) <br> [Paper](https://arxiv.org/abs/2406.03482)|[//]: #06/11
|[ZipCache: Accurate and Efficient KV Cache Quantization with Salient Token Identification](https://arxiv.org/abs/2405.14256) <br> Yefei He, Luoming Zhang, Weijia Wu, Jing Liu, Hong Zhou, Bohan Zhuang |<img width="1002" alt="image" src="figures/zipcache.png"> |[Paper](https://arxiv.org/abs/2405.14256)| [//]: #05/29

#### Hardware/System
| Title & Authors | Introduction | Links |
|:--|  :----: | :---:|
|[PowerInfer-2: Fast Large Language Model Inference on a Smartphone](https://arxiv.org/abs/2406.06282) <br> Zhenliang Xue, Yixin Song, Zeyu Mi, Le Chen, Yubin Xia, Haibo Chen |<img width="1002" alt="image" src="https://arxiv.org/html/2406.06282v1/x3.png"> |[Paper](https://arxiv.org/abs/2406.06282)|[//]: #06/11
|[![Publish](https://img.shields.io/badge/Conference-OSDI'24-blue)]()<br>[Parrot: Efficient Serving of LLM-based Applications with Semantic Variable](https://arxiv.org/abs/2405.19888) <br> Chaofan Lin, Zhenhua Han, Chengruidong Zhang, Yuqing Yang, Fan Yang, Chen Chen, Lili Qiu |<img width="1002" alt="image" src="figures/parrot.png"> |[Paper](https://arxiv.org/abs/2405.19888)| [//]: #05/31

#### Tuning
| Title & Authors | Introduction | Links |
|:--|  :----: | :---:|
|[![Star](https://img.shields.io/github/stars/gccnlp/Light-PEFT.svg?style=social&label=Star)](https://github.com/gccnlp/Light-PEFT)[![Publish](https://img.shields.io/badge/Conference-ACL'24%20Findings-blue)]()<br>[Light-PEFT: Lightening Parameter-Efficient Fine-Tuning via Early Pruning](https://arxiv.org/abs/2406.03792) <br> Naibin Gu, Peng Fu, Xiyu Liu, Bowen Shen, Zheng Lin, Weiping Wang |<img width="1002" alt="image" src="https://arxiv.org/html/2406.03792v1/x5.png"> |[Github](https://github.com/gccnlp/Light-PEFT) <br> [Paper](https://arxiv.org/abs/2406.03792)|[//]: #06/12
|[Zeroth-Order Fine-Tuning of LLMs with Extreme Sparsity](https://arxiv.org/abs/2406.02913) <br> Wentao Guo, Jikai Long, Yimeng Zeng, Zirui Liu, Xinyu Yang, Yide Ran, Jacob R. Gardner, Osbert Bastani, Christopher De Sa, Xiaodong Yu, Beidi Chen, Zhaozhuo Xu |<img width="1002" alt="image" src="https://arxiv.org/html/2406.02913v1/x4.png"> |[Paper](https://arxiv.org/abs/2406.02913)|[//]: #06/11
 
#### 💮 Contributing

If you'd like to include your paper, or need to update any details such as conference information or code URLs, please feel free to submit a pull request. You can generate the required markdown format for each paper by filling in the information in `generate_item.py` and execute `python generate_item.py`. We warmly appreciate your contributions to this list. Alternatively, you can email me with the links to your paper and code, and I would add your paper to the list at my earliest convenience. 





