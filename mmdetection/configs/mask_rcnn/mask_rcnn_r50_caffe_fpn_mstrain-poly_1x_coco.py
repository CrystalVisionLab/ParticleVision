_base_ = './mask_rcnn_r50_fpn_1x_coco.py'
model = dict(
    backbone=dict(
        norm_cfg=dict(requires_grad=False),
        style='caffe',
        init_cfg=dict(
            type='Pretrained',
            checkpoint='open-mmlab://detectron2/resnet50_caffe')))
# use caffe img_norm
img_norm_cfg = dict(
    mean=[89.524, 89.480, 89.481], std=[34.755, 34.718, 34.718], to_rgb=False)
    #mean=[103.530, 116.280, 123.675], std=[1.0, 1.0, 1.0], to_rgb=False)
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='LoadAnnotations',
        with_bbox=True,
        with_mask=True,
        poly2mask=False),
    dict(
        type='Resize',
        img_scale=(1650, 1275),
        #img_scale=[(1333, 640), (1333, 672), (1333, 704), (1333, 736),
        #           (1333, 768), (1333, 800)],
        #img_scale=[(2200, 1700), (1333, 672), (1333, 704), (1333, 736),
        #           (1333, 768), (1333, 800)],
        #img_scale=(2200, 1700),
        multiscale_mode='value',
        keep_ratio=True),
    #dict(type='Albu', transforms = [{"type": 'RandomRotate90'}]),# 旋转数据增强
    dict(type='RandomFlip', flip_ratio=0.5), # 翻转数据增强
    #dict(type='RandomAffine',max_rotate_degree=180.0),
    dict(type='Corrupt',corruption='defocus_blur',severity=1), #失焦噪声
    #dict(type='Corrupt',corruption='glass_blur',severity=1),
    #dict(type='Expand'),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='Pad', size_divisor=32),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_bboxes', 'gt_labels', 'gt_masks']),
]
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='MultiScaleFlipAug',
        #img_scale=(1333, 800),
        img_scale=(1650, 1275),
        #img_scale=(2200, 1700),
        flip=False,
        transforms=[
            dict(type='Resize', keep_ratio=True),
            dict(type='RandomFlip'),
            dict(type='Normalize', **img_norm_cfg),
            dict(type='Pad', size_divisor=32),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img']),
        ])
]
data = dict(
    train=dict(pipeline=train_pipeline),
    val=dict(pipeline=test_pipeline),
    test=dict(pipeline=test_pipeline))
