# Position-Prediction-Pretraining-Pytorch
**Pytorch Implementation of : Position Prediction as an Effective Pretraining Strategy**   
https://arxiv.org/abs/2207.07611   
https://proceedings.mlr.press/v162/zhai22a.html     
<img src="https://github.com/arshadshk/Position-Prediction-Pretraining-MP3/blob/main/images/title.png">
<br>

## About  
This is an unofficial implementation/replication built on top of [DeiT]("https://github.com/facebookresearch/deit") and [timm (pytorch-image-transformers)]("https://github.com/rwightman/pytorch-image-models") and is limited to **vision models**. Vision model(ViT) in *timm* is extended to support Attention Masking, Position Prediction and Position loss, whereas *DieT* is used for required pretraining configurations that the authors have used( page4 section4.2 ).
In this paper, the authors propose simple alternative to content reconstruction – that of predicting locations from content, without providing positional information for it. Doing so requires the Transformer to understand the positional relationships between different parts of the input, from their content alone. This amounts
to an efficient implementation where the pretext task is a classification problem among all possible positions for each input token. The paper contains both Vision and Speech benchmarks, but this repo only supports vision models.  
<br>

## Usage 
Clone this repo, and then update the submoules/sub-repos. Make sure to use DieT and timm from the submodules provided here, as the original versions dont support attention masking, position prediction and losses that were present in the paper.

        git submodule update --init --recursive     
<br>

### Model  
```python
import torch
import sys
sys.path.append("./pytorch-image-models/")

from timm.models import create_model 

model = create_model(   
                        model_name= "deit_small_patch4_32",
                        pretrained=False,
                        num_classes=100,
                        drop_rate=0.3,
                        drop_path_rate=0.1,
                        drop_block_rate=None,
                        img_size=32,
                        attn_mask=True,
                        eta=0.75,       
                        patch_stride=4
                    )
B,C,H,W = 64,3,32,32
out = model( torch.randn(B,C,H,W) )
print( out.shape )
# torch.Size([64, 65, 64]) 
# (batch, cls + patches, position_logits) 
# N:patches and +1 for cls
```
### Pretraining
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
<br>

## Finetunning  (WIP)
<br>

## Results
Results from paper : 
<img src=https://github.com/arshadshk/Position-Prediction-Pretraining-MP3/blob/main/images/results.png>
<br>
<br>
Results from running this repo:  
Dataset : CIFAR 100  
epochs : 362  
eta : 0.75  
( $\eta = 0.75$ )   
checkpoint link : https://www.kaggle.com/datasets/arshadshaikh7/pretrainedvit   
script to plot results :     
<img src="https://github.com/arshadshk/Position-Prediction-Pretraining/blob/main/images/Screen%20Shot%202023-01-13%20at%209.29.31%20PM.png" width="350">
  
<br>

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





