# MediLab

![Medilab Website](https://github.com/chetanpandey1266/HackInIndia/blob/master/medilab.gif)

## Table of Contents
- [Introduction]()
- [Implementation]()
- [Training]()
- [Installation]()
- [How to Use]()

## Introduction:
Medilab is an interactive web application that can make diagnosis of pulmonary tuberculosis much easier than before. With a deep learning backend, our web app will diagnosis pulmonary tuberculosis within seconds using x-ray chest image of the patient.

## Implementations

- Used pretrained resnet34 model
- Cross Entropy Loss 
- Simple Augmentations: flip, rotate, zoom, lightning, normalize
- Used `max_lr = slice(range)` to apply smaller learning rates to initial layers and larger to later ones.

## Training


## Installation 

### Prerequisites

`fastai`

`fastai.vision`

`numpy`

### Models

[Resnet34](https://drive.google.com/file/d/1-183IuG42Sh6p4Kk6ok_DJw_PGtbNVSl/view)

[EfficientNetb3](https://drive.google.com/file/d/1F2RamM03oBahviwY93XCnrpNuTKobMzn/view?usp=sharing)

## How to Use

##### 1. Using Webapp

[WebApp Link](#)
You can simply use the web app to register yourself and then pass into your x-ray chest image to get the result

##### 2. Directly from python script
Pretrained models can be downloaded from links provided above.
Use the scripts provided in `Python Scripts` folder to run the model.
Pass in the image model path and image path to get the result


