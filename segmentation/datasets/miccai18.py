from mmseg.datasets import DATASETS, CustomDataset

@DATASETS.register_module()
class Miccai18Dataset(CustomDataset):
    """Miccai18 dataset
    
    0 stands for background (background-tissue), 
    which is included in the 12 categories. 
    
    `reduce_zero_label` is fixed to False.
    """

    CLASSES = (
        'background',
        'instrument-shaft',
        'instrument-clasper',
        'instrument-wrist',
        'kidney-parenchyma',
        'covered-kidney',
        'thread',
        'clamps',
        'suturing-needle',
        'suction-instrument',
        'small-intestine',
        'ultrasound-probe'
    )

    PALETTE = [
        [0, 0, 0],
        [0, 255, 0],
        [0, 255, 255],
        [125, 255, 12],
        [255, 55, 0],
        [24, 55, 125],
        [187, 155, 25],
        [0, 255, 125],
        [255, 255, 125],
        [123, 15, 175],
        [124, 155, 5],
        [12, 255, 141]
    ]

    def __init__(self, **kwargs):
        super(Miccai18Dataset, self).__init__(
            img_suffix='.png', 
            seg_map_suffix='.png',
            reduce_zero_label=False,
            **kwargs)