# DPPs Detection

This repo provided a new method and idea for the detection, segmentation, classification, and quantitative analysis of four dispersed phase particles - "DPPs" (agglomeration, bubble, crystal, and droplet) in chemical multi-phase flow processes.

## Quick Start

Install packages :

```
python -m pip install -r requirements.txt
```

Install mmdetection:

```
pip install mmcv-full
pip install mmcv-full -f https://download.openmmlab.com/mmcv/dist/{cu_version}/{torch_version}/index.html
```

Get source code:

```
git clone https://github.com/CrystalVisionLab/ParticleVision.git
```

Compile source code:

```
python setup.py develop
```

Download pretrained model from: 

- 百度云：https://pan.baidu.com/s/18dWehstHxixFbIP93sNesg, 提取码: bb6r ；
- Google Driver: TBD

Copy pretrained model to mmdetection/work_dirs/mask_rcnn_r50_caffe_fpn_mstrain-poly_1xSF.

Detect crystal: 

```
python detect.py --img_file ./val/IMG.png --out_file ./result.jpg
```



## Main Functionality

- Single image detection:

  ```
  python detect.py --img_file ./val/IMG.png --out_file ./result.jpg
  ```

  

- Multiple images detection:

  First, detect and get npy file:

  ```
  python batch_detect.py
  ```

  Then, analysis the detect result:

  ```
  python batch_ana.py
  ```

  Finally, you can visualize the analysis result by using the following demand:

  ```
  python batch_visualize.py
  ```

  

## Training Model

- Generate json in coco style:

  ```
  python generate_json.py
  ```

- Start training:

  ```
  cd mmdetection
  python tools/train.py configs/mask_rcnn_r50_caffe_fpn_mstrain-poly_1xSF.py
  ```



## Evaluation

See offical documents of mmdetection:  [open-mmlab/mmdetection: OpenMMLab Detection Toolbox and Benchmark (github.com)](https://github.com/open-mmlab/mmdetection)



## Acknowledgement

The framework of this repo is based on open source object detection toolbox: MMDetection.
