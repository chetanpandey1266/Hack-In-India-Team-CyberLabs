from fastai import * 
from fastai.vision import *


im_path = # location of image(string)

model_path1 = # loaction of model(string)
model_path2 = # location of model(string)

learn1 = load_learner(model_path1, "model.pkl")
learn2 = load_learner(model_path2, "resnet50.pkl")


p1 = learn1.predict(open_image(im_path))[2].numpy().astype(np.float32)
p2 = learn2.predict(open_image(im_path))[2].numpy().astype(np.float32)

w1 = 0.4
w2 = 0.6

final_output = w1*p1 + w2*p2

final_output = final_output.tolist()

print(final_output)

# Index 0 gives probability of abnormal case and Index 1 gives probability of normal case
