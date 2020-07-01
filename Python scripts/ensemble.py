from fastai import * 
from fastai import *


im_path = # location of image(string)

model_path1 = # loaction of model(string)
model_path2 = # location of model(string)

learn1 = load_learner(model_path1)
learn2 = load_learner(model_path2)


p1 = learn1.predict(open_image(im_path))[2].numpy().tolist()
p2 = learn2.predict(open_image(im_path))[2].numpy().tolist()

w1 = 0.4
w2 = 0.6

final_result = p1*w1 + p2*w2
