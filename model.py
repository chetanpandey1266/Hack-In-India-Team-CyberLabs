from fastai import *
from fastai.vision import *
!pip install efficientnet-pytorch

im_path = # location of image(string)

model_path = # loaction of model(string)

learn = load_learner(model_path)


learn.predict(open_image(im_path))[2].numpy().tolist()
