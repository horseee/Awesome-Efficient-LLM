# Efficient-PLM

A curated list for **Efficient Pre-trained Language Models**:
  - [Knowledge Distillation](#knowledge-distillation)
  - [Network Pruning](#network-pruning)
  - [Quantization](#quantization)
  - [Inference Acceleration](#inference-acceleration)
  - [Others](#others)

This part is still under construction to include papers published from 2018-2023.



## Knowledge Distillation
* [![Publish](https://img.shields.io/badge/Conference-ACL'23-blue)]() [![Star](https://img.shields.io/github/stars/nitaytech/KD4Gen.svg?style=social&label=Star)](https://github.com/nitaytech/KD4Gen) [A Systematic Study of Knowledge Distillation for Natural Language Generation with Pseudo-Target Training](https://arxiv.org/abs/2305.02031). Nitay Calderon, Subhabrata Mukherjee, Roi Reichart, Amir Kantor. [[Paper]](https://arxiv.org/abs/2305.02031)[[Github]](https://github.com/nitaytech/KD4Gen)
* [![Publish](https://img.shields.io/badge/Conference-ACL'23-blue)]() [![Star](https://img.shields.io/github/stars/twinkle0331/LGTM.svg?style=social&label=Star)](https://github.com/twinkle0331/LGTM) [Tailoring Instructions to Student's Learning Levels Boosts Knowledge Distillation](https://arxiv.org/abs/2305.09651). Yuxin Ren, Zihan Zhong, Xingjian Shi, Yi Zhu, Chun Yuan, Mu Li. [[Paper]](https://arxiv.org/abs/2305.09651)[[Github]](https://github.com/twinkle0331/LGTM)
* [![Publish](https://img.shields.io/badge/Conference-ACL'23-blue)]() [![Star](https://img.shields.io/github/stars/MANGA-UOFA/fdistill.svg?style=social&label=Star)](https://github.com/MANGA-UOFA/fdistill) [f-Divergence Minimization for Sequence-Level Knowledge Distillation](https://aclanthology.org/2023.acl-long.605/). Yuqiao Wen, Zichao Li, Wenyu Du, Lili Mou. [[Paper]](https://aclanthology.org/2023.acl-long.605/)[[Github]](https://github.com/MANGA-UOFA/fdistill)
* [![Publish](https://img.shields.io/badge/Conference-ACL'23-blue)]() [![Star](https://img.shields.io/github/stars/brucewsy/AD-KD.svg?style=social&label=Star)](https://github.com/brucewsy/AD-KD) [AD-KD: Attribution-Driven Knowledge Distillation for Language Model Compression](https://arxiv.org/abs/2305.10010). Siyue Wu, Hongzhan Chen, Xiaojun Quan, Qifan Wang, Rui Wang. [[Paper]](https://arxiv.org/abs/2305.10010)[[Github]](https://github.com/brucewsy/AD-KD)
* [![Publish](https://img.shields.io/badge/Conference-ACL'23-blue)]() [![Star](https://img.shields.io/github/stars/GeneZC/MiniMoE.svg?style=social&label=Star)](https://github.com/GeneZC/MiniMoE) [Lifting the Curse of Capacity Gap in Distilling Language Models](https://arxiv.org/abs/2305.12129). Chen Zhang, Yang Yang, Jiahao Liu, Jingang Wang, Yunsen Xian, Benyou Wang, Dawei Song. [[Paper]](https://arxiv.org/abs/2305.12129)[[Github]](https://github.com/GeneZC/MiniMoE)
* [![Publish](https://img.shields.io/badge/Conference-ACL'23-blue)]() [![Star](https://img.shields.io/github/stars/thunlp-mt/dbkd-plm.svg?style=social&label=Star)](https://github.com/thunlp-mt/dbkd-plm) [Bridging the Gap between Decision and Logits in Decision-based Knowledge Distillation for Pre-trained Language Models](https://arxiv.org/abs/2306.08909). Qinhong Zhou, Zonghan Yang, Peng Li, Yang Liu. [[Paper]](https://arxiv.org/abs/2306.08909)[[Github]](https://github.com/thunlp-mt/dbkd-plm)
* [![Publish](https://img.shields.io/badge/Conference-ACL'23-blue)]() [Teaching Small Language Models to Reason](https://arxiv.org/abs/2212.08410). Lucie Charlotte Magister, Jonathan Mallinson, Jakub Adamek, Eric Malmi, Aliaksei Severyn. [[Paper]](https://arxiv.org/abs/2212.08410)
* [![Publish](https://img.shields.io/badge/Conference-ACL'23-blue)]() [![Star](https://img.shields.io/github/stars/mainlp/How-to-distill-your-BERT.svg?style=social&label=Star)](https://github.com/mainlp/How-to-distill-your-BERT) [How to Distill your BERT: An Empirical Study on the Impact of Weight Initialisation and Distillation Objectives](https://arxiv.org/abs/2305.15032). Xinpeng Wang, Leonie Weissweiler, Hinrich Schütze, Barbara Plank. [[Paper]](https://arxiv.org/abs/2305.15032)[[Github]](https://github.com/mainlp/How-to-distill-your-BERT)
* [![Publish](https://img.shields.io/badge/Conference-ACL'23-blue)]() [ReAugKD: Retrieval-augmented knowledge distillation for pre-trained language models](https://www.amazon.science/publications/reaugkd-retrieval-augmented-knowledge-distillation-for-pre-trained-language-models). Jianyi Zhang, Aashiq Muhamed, Aditya Anantharaman, Guoyin Wang, Changyou Chen, Kai Zhong, Qingjun Cui, Yi Xu, Belinda Zeng, Trishul Chilimbi, Yiran Chen. [[Paper]](https://www.amazon.science/publications/reaugkd-retrieval-augmented-knowledge-distillation-for-pre-trained-language-models)



## Network Pruning
* [![Publish](https://img.shields.io/badge/Conference-ACL'23-blue)]() [![Star](https://img.shields.io/github/stars/kongds/SMP.svg?style=social&label=Star)](https://github.com/allenai/kongds/SMP) [Pruning Pre-trained Language Models Without Fine-Tuning](https://aclanthology.org/2023.acl-long.35/). Ting Jiang, Deqing Wang, Fuzhen Zhuang, Ruobing Xie, Feng Xia. [[Paper]](https://aclanthology.org/2023.acl-long.35/)) [[Github]](https://github.com/kongds/SMP) 
* [![Publish](https://img.shields.io/badge/Conference-ACL'23-blue)]() [![Star](https://img.shields.io/github/stars/airaria/GRAIN.svg?style=social&label=Star)](https://github.com/airaria/GRAIN) [Gradient-based Intra-attention Pruning on Pre-trained Language Models](https://arxiv.org/abs/2212.07634). Ziqing Yang, Yiming Cui, Xin Yao, Shijin Wang. [[Paper]](https://arxiv.org/abs/2212.07634)[[Github]](https://github.com/airaria/GRAIN)
* [![Publish](https://img.shields.io/badge/Conference-ACL'23-blue)]() [![Star](https://img.shields.io/github/stars/naver/nllb-pruning.svg?style=social&label=Star)](https://github.com/naver/nllb-pruning) [Memory-efficient NLLB-200: Language-specific Expert Pruning of a Massively Multilingual Machine Translation Model](https://arxiv.org/abs/2212.09811). Yeskendir Koishekenov, Alexandre Berard, Vassilina Nikoulina. [[Paper]](https://arxiv.org/abs/2212.09811)[[Github]](https://github.com/naver/nllb-pruning)
* [![Publish](https://img.shields.io/badge/Conference-ACL'23%20Findings-blue)]() [Structured Pruning for Efficient Generative Pre-trained Language Models](https://aclanthology.org/2023.findings-acl.692/). 
Chaofan Tao, Lu Hou, Haoli Bai, Jiansheng Wei, Xin Jiang, Qun Liu, Ping Luo, Ngai Wong. [[Paper]](https://aclanthology.org/2023.findings-acl.692/) 

## Quantization
* [![Publish](https://img.shields.io/badge/Conference-ACL'23-blue)]() [Self-Distilled Quantization: Achieving High Compression Rates in Transformer-Based Language Models](https://aclanthology.org/2023.acl-short.114/). James O’Neill, Sourav Dutta. [[Paper]](https://aclanthology.org/2023.acl-short.114/)

## Inference Acceleration
* [![Publish](https://img.shields.io/badge/Conference-ACL'23-blue)]() [![Star](https://img.shields.io/github/stars/dropreg/DEER.svg?style=social&label=Star)](https://github.com/dropreg/DEER) [Dynamic and Efficient Inference for Text Generation via BERT Family](https://aclanthology.org/2023.acl-long.162/). Xiaobo Liang, Juntao Li, Lijun Wu, Ziqiang Cao, Min Zhang. [[Paper]](https://aclanthology.org/2023.acl-long.162/)[[Github]](https://github.com/dropreg/DEER)

## Others
* [![Publish](https://img.shields.io/badge/Conference-ACL'23-blue)]() [PuMer: Pruning and Merging Tokens for Efficient Vision Language Models](https://arxiv.org/abs/2305.17530). Qingqing Cao, Bhargavi Paranjape, Hannaneh Hajishirzi. [[Paper]](https://arxiv.org/abs/2305.17530)