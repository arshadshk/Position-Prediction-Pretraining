# Position-Prediction-Pretraining-Pytorch
**Pytorch Implementation of : Position Prediction as an Effective Pretraining Strategy**   
https://arxiv.org/abs/2207.07611   
https://proceedings.mlr.press/v162/zhai22a.html     

<br>
<br>
<img src="https://github.com/arshadshk/Position-Prediction-Pretraining-MP3/blob/main/images/title.png">
<br>

## About  
This is an unofficial implementation/replication built on top of [DeiT]("https://github.com/facebookresearch/deit") and [timm (pytorch-image-transformers)]("https://github.com/rwightman/pytorch-image-models") and is limited to **vision models**. Vision model(ViT) in *timm* is extended to support Attention Masking, Position Prediction and Position loss, whereas *DieT* is used for required pretraining configurations that the authors have used( page4 section4.2 ).
In this paper, the authors propose simple alternative to content reconstruction – that of predicting locations from content, without providing positional information for it. Doing so requires the Transformer to understand the positional relationships between different parts of the input, from their content alone. This amounts
to an efficient implementation where the pretext task is a classification problem among all possible positions for each input token. The paper contains both Vision and Speech benchmarks, but this repo only supports vision models.  

## Usage 
Clone this repo, and then update the submoules/sub-repos. Make sure to use DieT and timm from the submodules provided here, as the original versions dont support attention masking, position prediction and losses that were present in the paper.

        git submodule update --init --recursive     


## Pretraining
Pretrainig on (CIFAR-100) dataset without distillation: 

        python3 deit/main.py    --attn_mask true  \
                                --eta 0.5  \
                                --patch_stride 4  \
                                --data-set CIFAR  \
                                --data-path ./data/cifar-100-python \
                                --datadownload true  \
                                --device cpu  \
                                --num_workers 0  \
                                --model deit_small_patch4_32  \
                                --smoothing 0  \
                                --mixup 0  \
                                --cutmix 0  \
                                --distillation-alpha 0  

Pretrainig using distillation: (WIP)

## Finetunning  (WIP)
<br>

## Results
Results from paper : 
<img src=https://github.com/arshadshk/Position-Prediction-Pretraining-MP3/blob/main/images/results.png>
<br>
Results from running this repo: (wip)


## Citations

```bibtex
@InProceedings{pmlr-v162-zhai22a,
  title = 	 {Position Prediction as an Effective Pretraining Strategy},
  author =       {Zhai, Shuangfei and Jaitly, Navdeep and Ramapuram, Jason and Busbridge, Dan and Likhomanenko, Tatiana and Cheng, Joseph Y and Talbott, Walter and Huang, Chen and Goh, Hanlin and Susskind, Joshua M},
  booktitle = 	 {Proceedings of the 39th International Conference on Machine Learning},
  pages = 	 {26010--26027},
  year = 	 {2022},
  pdf = 	 {https://proceedings.mlr.press/v162/zhai22a/zhai22a.pdf},
  url = 	 {https://proceedings.mlr.press/v162/zhai22a.html},
```





