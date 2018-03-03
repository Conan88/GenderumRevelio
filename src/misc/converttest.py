from keras.preprocessing import text
import numpy as np
from keras.datasets import imdb


malepath = "../../newmale.txt"
femalepath = "../../newfemale.txt"

female_data = []
male_data = []

print("Start")

with open(malepath, encoding="latin-1") as file:
    for line in file:
        if line.strip() == "":
            print("empty")
        else:
            male_data.append(line)

with open(femalepath, encoding="latin-1") as file:
    for line in file:
        if line.strip() == "":
            print("empty")
        else:
            female_data.append(line)

malelength = len(male_data)
femalelength = len(female_data)
print("male: " + str(malelength))
print("female:" + str(femalelength))

print("Sentences to array")

bothgenders = male_data + female_data

one_hot_array = []
for ting in bothgenders:
    a = text.one_hot(ting, n=720000, filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n', lower=True, split=" ")
    one_hot_array.append(a)

print("Done with one_hot conversion")

np.save("hot_numpy", np.array(one_hot_array))
