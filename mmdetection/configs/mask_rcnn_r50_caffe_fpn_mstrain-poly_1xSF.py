# The new config inherits a base config to highlight the necessary modification
_base_ = 'mask_rcnn/mask_rcnn_r50_caffe_fpn_mstrain-poly_1x_coco.py'

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=4),
        mask_head=dict(num_classes=4)))

# Modify dataset related settings
dataset_type = 'COCODataset'
classes = ('A','B','C','D')
data = dict(
    samples_per_gpu=2,
    workers_per_gpu=2,
    train=dict(
        img_prefix='C:/Users/Administrator/Desktop/CystalDetection-master/train',
        classes=classes,
        ann_file='C:/Users/Administrator/Desktop/CystalDetection-master/train.json'),
    val=dict(
        img_prefix='C:/Users/Administrator/Desktop/CystalDetection-master/val',
        classes=classes,
        ann_file='C:/Users/Administrator/Desktop/CystalDetection-master/val.json'),
    test=dict(
        img_prefix='C:/Users/Administrator/Desktop/CystalDetection-master/val',
        classes=classes,
        ann_file='C:/Users/Administrator/Desktop/CystalDetection-master/val.json'),
    )

