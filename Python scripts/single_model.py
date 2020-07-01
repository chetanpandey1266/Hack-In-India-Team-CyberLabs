from fastai import *
from fastai.vision import *


im_path = # location of image(string)

model_path = # loaction of model(string)

learn = load_learner(model_path, "model.pkl")


pred = learn.predict(open_image(im_path))[2].numpy().tolist()

print(pred)
