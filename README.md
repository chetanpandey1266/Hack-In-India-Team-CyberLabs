# MediLab

![Medilab Website](https://github.com/chetanpandey1266/HackInIndia/blob/master/gif/website.gif)

## Table of Contents
- [Introduction](#Introduction)
- [Implementation](#Implementations)
- [Training](#Training)
- [Installation](#Prerequisites)
- [How to Use](#How_to_Use)

## Introduction:
Medilab is an interactive web application that can make diagnosis of pulmonary tuberculosis much easier than before. With a deep learning backend, our web app will diagnosis pulmonary tuberculosis within seconds using x-ray chest image of the patient.

## Implementations

- Used pretrained resnet34 model
- Cross Entropy Loss 
- Simple Augmentations: flip, rotate, zoom, lightning, normalize
- Used `max_lr = slice(range)` to apply smaller learning rates to initial layers and larger to later ones.

## Training
- The IPython notebooks were trained on Google Colab with GPU(Tesla K80) enabled. The trained models have not been uploaded on to Github.
- 640 images were used to train, and 160 to validate the results
- Resnet34 architecture is trained on this dataset and quite good results are obtained.
### Results
- The Resnet34 model trained over 20 epochs decreased the error rate from 0.518 to 0.081
- Learning Rate curve 
- Confusion Matrix
- Accuracy measured = 91.87%

## Installation 

### Prerequisites

`fastai`

`fastai.vision`

`numpy`

### Models

[Resnet34](https://drive.google.com/file/d/1-183IuG42Sh6p4Kk6ok_DJw_PGtbNVSl/view)

[EfficientNetb3](https://drive.google.com/file/d/1F2RamM03oBahviwY93XCnrpNuTKobMzn/view?usp=sharing)

## How_to_Use

##### 1. Using Webapp

[WebApp Link: App is Deployed here.](https://tbdetector.herokuapp.com/)

You can simply use the web app to register yourself and then pass into your x-ray chest image to get the result.
The backend of the file has been implemented in nodejs, express and mongodb. The forntend is pure HTML with BootStrap and jquery and using fetch api.

##### 2. Directly from python script
Pretrained models can be downloaded from links provided above.

Use the scripts provided in `Python Scripts` folder to run the model.
Pass in the image model path and image path to get the result


