# Position-Prediction-Pretraining-MP3
Position Prediction as an Effective Pretraining Strategy  

This repo is built on top of DieT and timm repos. timm contains the ViT models and DieT is used setting up needed pretraining configurations easily. 

Clone this repo along with the submoules for ViT models.  

        git submodule update --init --recursive     
( Make sure to use DieT and timm from the submodules provided here, as the original versions dont support attention masking, position prediction and losses that were present in the paper )

Pretrainig the model : 
        python3 deit/main.py  --attn_mask true \
                                --eta 0.5 \
                                --patch_stride 4 \
                                --data-setCIFAR \
                                --data-path /Users/arshad/deit/Position-Prediction-Pretraining-MP3/data/cifar-100-python \
                                --datadownload true \
                                --device cpu \
                                --num_workers 0 \
                                --modeldeit_small_patch4_32 \
                                --smoothing 0 \
                                --mixup 0 \
                                --cutmix 0 \
                                --distillation-alpha0 \
