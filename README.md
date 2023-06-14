# Awesome-Efficient-LLM


A curated list for **Efficient Large Language Models**:
  - [Knowledge Distillation](#knowledge-distillation)
  - [Network Pruning](#network-pruning)
  - [Quantization](#quantization)
  - [Inference Acceleration](#inference-acceleration)
  - [Others](#others)


## Knowledge Distillation
| Title & Authors | Introduction | Links |
|:----|  :----: | :---:|
| [![Star](https://img.shields.io/github/stars/mbzuai-nlp/LaMini-LM.svg?style=social&label=Star)](https://github.com/mbzuai-nlp/LaMini-LM) <br> [LaMini-LM: A Diverse Herd of Distilled Models from Large-Scale Instructions](https://github.com/mbzuai-nlp/LaMini-LM) <br>Minghao Wu, Abdul Waheed, Chiyu Zhang, Muhammad Abdul-Mageed, Alham Fikri Aji | <img width="1002" alt="image" src="https://github.com/mbzuai-nlp/LaMini-LM/blob/main/images/lamini-pipeline.drawio.png"> | [Github](https://github.com/mbzuai-nlp/LaMini-LM) [paper](https://arxiv.org/abs/2304.14402) |
| [Distilling Step-by-Step! Outperforming Larger Language Models with Less Training Data and Smaller Model Sizes](https://arxiv.org/abs/2305.02301) <br> Cheng-Yu Hsieh, Chun-Liang Li, Chih-Kuan Yeh, Hootan Nakhost, Yasuhisa Fujii, Alexander Ratner, Ranjay Krishna, Chen-Yu Lee, Tomas Pfister | <img width="2000" alt="image" src="figures/Distill_step_by_step.png">| [Paper](https://arxiv.org/abs/2305.02301) |
| [![Star](https://img.shields.io/github/stars/ananyahjha93/llm-distill.svg?style=social&label=Star)](https://github.com/ananyahjha93/llm-distill) <br> [Large Language Model Distillation Doesn't Need a Teacher](https://arxiv.org/abs/2305.14864) <br> Ananya Harsh Jha, Dirk Groeneveld, Emma Strubell, Iz Beltagy </br> | <img width="2000" alt="image" src="figures/TeacherFreeLLM.png"> | [Github](https://github.com/ananyahjha93/llm-distill) [paper](https://arxiv.org/abs/2305.14864) |
| [The False Promise of Imitating Proprietary LLMs](https://arxiv.org/abs/2305.15717) <br> Arnav Gudibande, Eric Wallace, Charlie Snell, Xinyang Geng, Hao Liu, Pieter Abbeel, Sergey Levine, Dawn Song | <img width="1000" alt="image" src="figures/FalsePromise.png"> | [Paper](https://arxiv.org/abs/2305.15717) |
|[![Star](https://img.shields.io/github/stars/jaehunjung1/impossible-distillation.svg?style=social&label=Star)](https://github.com/jaehunjung1/impossible-distillation) <br>[Impossible Distillation: from Low-Quality Model to High-Quality Dataset & Model for Summarization and Paraphrasing](https://arxiv.org/abs/2305.16635) <br> Jaehun Jung, Peter West, Liwei Jiang, Faeze Brahman, Ximing Lu, Jillian Fisher, Taylor Sorensen, Yejin Choi |<img width="1002" alt="image" src="figures/impossible_distillation.png"> |[Github](https://github.com/jaehunjung1/impossible-distillation) [paper](https://arxiv.org/abs/2305.16635) |



## Network Pruning
| Title & Authors | Introduction | Links |
|:----|  :----: | :---:|
| [![Star](https://img.shields.io/github/stars/IST-DASLab/sparsegpt.svg?style=social&label=Star)](https://github.com/IST-DASLab/sparsegpt) <br> [SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot](https://github.com/IST-DASLab/sparsegpt) <br> Elias Frantar, Dan Alistarh| <img width="522" alt="image" src="figures/sparsegpt.png"> |[Github](https://github.com/IST-DASLab/sparsegpt) [paper](https://arxiv.org/abs/2301.00774) |
| [![Star](https://img.shields.io/github/stars/horseee/LLM-Pruner.svg?style=social&label=Star)](https://github.com/horseee/LLM-Pruner) <br>[LLM-Pruner: On the Structural Pruning of Large Language Models](https://arxiv.org/abs/2305.11627) <br> Xinyin Ma, Gongfan Fang, Xinchao Wang | <img width="1061" alt="image" src="figures/llm_pruner.png">| [Github](https://github.com/horseee/LLM-Pruner) [paper](https://arxiv.org/abs/2305.11627)|


## Quantization
| Title & Authors | Introduction | Links |
|:--|  :----: | :---:|
| [![Star](https://img.shields.io/github/stars/qwopqwop200/GPTQ-for-LLaMa.svg?style=social&label=Star)](https://github.com/qwopqwop200/GPTQ-for-LLaMa) <br>[GPTQ-for-LLaMA](https://github.com/qwopqwop200/GPTQ-for-LLaMa): 4 bits quantization of LLaMA using GPTQ. | <img width="102" alt="image" src="https://user-images.githubusercontent.com/64115820/235287009-2d07bba8-9b85-4973-9e06-2a3c28777f06.png"> |[Github](https://github.com/qwopqwop200/GPTQ-for-LLaMa)|
| [Outlier Suppression+: Accurate quantization of large language models by equivalent and optimal shifting and scaling](https://arxiv.org/abs/2304.09145v1) <br> Xiuying Wei , Yunchen Zhang, Yuhang Li, Xiangguo Zhang, Ruihao Gong, Jinyang Guo, Xianglong Liu|  <img width="1102" alt="image" src="figures/outliersuppression.png"> | [Paper](https://arxiv.org/abs/2304.09145v1)|
| [![Star](https://img.shields.io/github/stars/hahnyuan/RPTQ4LLM.svg?style=social&label=Star)](https://github.com/hahnyuan/RPTQ4LLM) <br>[RPTQ: Reorder-based Post-training Quantization for Large Language Models](https://arxiv.org/abs/2304.01089) <br> Zhihang Yuan and Lin Niu and Jiawei Liu and Wenyu Liu and Xinggang Wang and Yuzhang Shang and Guangyu Sun and Qiang Wu and Jiaxiang Wu and Bingzhe Wu | ![](https://github.com/hahnyuan/RPTQ4LLM/blob/master/ims/cover.png) | <br>[Github](https://github.com/hahnyuan/RPTQ4LLM)</br> [Paper](https://arxiv.org/abs/2304.01089) |
| [![Star](https://img.shields.io/github/stars/artidoro/qlora.svg?style=social&label=Star)](https://github.com/artidoro/qlora) <br>[QLoRA: Efficient Finetuning of Quantized LLMs](https://arxiv.org/abs/2305.14314) <br> Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, Luke Zettlemoyer | ![](figures/qlora.png) | <br>[Github](https://github.com/artidoro/qlora)</br> [Paper](https://arxiv.org/abs/2305.14314) |
| [SqueezeLLM: Dense-and-Sparse Quantization](https://arxiv.org/pdf/2306.07629.pdf) <br>Sehoon Kim, Coleman Hooper, Amir Gholami, Zhen Dong, Xiuyu Li, Sheng Shen, Michael W. Mahoney, Kurt Keutzer | <img width="1102" alt="image" src="figures/SqueezeLLM.png"> | [Paper](https://arxiv.org/pdf/2306.07629.pdf)|
|[ZeroQuant-V2: Exploring Post-training Quantization in LLMs from Comprehensive Study to Low Rank Compensation](https://arxiv.org/abs/2303.08302) <br> Zhewei Yao, Xiaoxia Wu, Cheng Li, Stephen Youn, Yuxiong He |<img width="1002" alt="image" src="figures/zeroquant-v2.png"> |[Paper](https://arxiv.org/abs/2303.08302)|
|[Integer or Floating Point? New Outlooks for Low-Bit Quantization on Large Language Models](https://arxiv.org/abs/2305.12356) <br> Yijia Zhang, Lingran Zhao, Shijie Cao, Wenqiang Wang, Ting Cao, Fan Yang, Mao Yang, Shanghang Zhang, Ningyi Xu |<img width="1002" alt="image" src="figures/MoFQ.png"> |[Paper](https://arxiv.org/abs/2305.12356)|
|[LLM-QAT: Data-Free Quantization Aware Training for Large Language Models](https://arxiv.org/abs/2305.17888) <br> Zechun Liu, Barlas Oguz, Changsheng Zhao, Ernie Chang, Pierre Stock, Yashar Mehdad, Yangyang Shi, Raghuraman Krishnamoorthi, Vikas Chandra |<img width="1002" alt="image" src="figures/LLM-QAT.png"> |[Paper](https://arxiv.org/abs/2305.17888)|



## Inference Acceleration
| Title & Authors | Introduction | Links |
|:--|  :----: | :---:|
| [![Star](https://img.shields.io/github/stars/microsoft/LMOps.svg?style=social&label=Star)](https://github.com/microsoft/LMOps) <br> [Inference with Reference: Lossless Acceleration of Large Language Models](https://arxiv.org/abs/2304.04487) <br> Nan Yang, Tao Ge, Liang Wang, Binxing Jiao, Daxin Jiang, Linjun Yang, Rangan Majumder, Furu Wei | <img width="800" alt="image" src="figures/llma.png"> | [Github](https://github.com/microsoft/LMOps) |
| [![Star](https://img.shields.io/github/stars/flexflow/FlexFlow.svg?style=social&label=Star)](https://github.com/flexflow/FlexFlow/tree/inference) <br> [SpecInfer: Accelerating Generative LLM Serving with Speculative Inference and Token Tree Verification](https://arxiv.org/abs/2305.0978) <br> Xupeng Miao, Gabriele Oliaro, Zhihao Zhang, Xinhao Cheng, Zeyu Wang, Rae Ying Yee Wong, Zhuoming Chen, Daiyaan Arfeen, Reyna Abhyankar, Zhihao Jia| <img width="2000" alt="image" src="https://github.com/flexflow/FlexFlow/blob/inference/img/overview.png">| [Github](https://github.com/flexflow/FlexFlow/tree/inference) <br> [paper](https://arxiv.org/abs/2305.09781) |
|[Scissorhands: Exploiting the Persistence of Importance Hypothesis for LLM KV Cache Compression at Test Time](https://arxiv.org/abs/2305.17118) <br> Zichang Liu, Aditya Desai, Fangshuo Liao, Weitao Wang, Victor Xie, Zhaozhuo Xu, Anastasios Kyrillidis, Anshumali Shrivastava |<img width="1002" alt="image" src="figures/Scissorhands.png"> |[Paper](https://arxiv.org/abs/2305.17118)|


## Others
| Title & Authors | Introduction | Links |
|:--|  :----: | :---:|
|[LLMZip: Lossless Text Compression using Large Language Models](https://arxiv.org/abs/2306.04050) <br> Chandra Shekhara Kaushik Valmeekam, Krishna Narayanan, Dileep Kalathil, Jean-Francois Chamberland, Srinivas Shakkottai |<img width="1002" alt="image" src="figures/LLMZip.png"> |[Paper](https://arxiv.org/abs/2306.04050) \| [Unofficial Github](https://github.com/erika-n/GPTzip)|
