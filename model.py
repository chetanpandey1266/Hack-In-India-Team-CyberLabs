from fastai import *
from fastai.vision import *


im_path = # location of image(string)

model_path = # loaction of model(string)

learn = load_learner(model_path)


learn.predict(open_image(im_path))
