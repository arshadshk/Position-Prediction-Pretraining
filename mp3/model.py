import sys
sys.path.append( "pytorch-image-models/" )

from timm.models import create_model


model = create_model(
    args.model,
    pretrained=False,
    num_classes=args.nb_classes,
    drop_rate=args.drop,
    drop_path_rate=args.drop_path,
    drop_block_rate=None,
    img_size=args.input_size
)