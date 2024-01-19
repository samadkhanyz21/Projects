
# Drowsiness Detection

The goal of the research is to identify driver tiredness and inform them at the appropriate moment to avoid any accidents. The problem at hand is to capture the driver’s facial images using an image sensor and to detect if they are in a drowsy state or not. The deep learning model is supposed to predict the probability of being drowsy or awake.

We use a `YOLOv8` model to predict whether a person feels drowsy or not based on whether the eyes are closed or open and if a yawn is detected or not. The project directly benefits the automotive sector, improves driving safety, and lowers the number of fatalities brought on by drowsy driving.

## Dataset Collection

We have `4 classes` namely: 
* `closed eye` 
* `closed mouth` 
* `open eye` 
* `open mouth`

The dataset was selected from a pre-classified image dataset found on `Roboflow`. This had around `2400 images` in the training data balanced equally across the four classes. We also validated our model on the training set.

## Requirements

* Torch
* seaborn
* Numpy
* Pillow
* Torchvision
* Matplotlib
* OpenCV-python
* Ultralytics (YOLOv8)
* pyyaml

I am using YOLOv8 extra large pretrained model (`yolov8x`). 

## Note

Due to computing issues, a kaggle notebook was created. Sole purpose of using kaggle was to use the resource of `GPU`. The configuration for both `custom_data.yaml` and `kaggle_data.yaml` is same. Only paths are changed so that the model can pick the labels for the images. Try to give/paste absolute paths to images.

## Yaml Data Configuration
train: ../data/train/images\
val: ../data/valid/images\
test: ../data/test/images

nc: 4\
names: ['closed_eye', 'closed_mouth', 'open_eye', 'open_mouth']







