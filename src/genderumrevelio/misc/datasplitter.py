import numpy as np

path = r"../../data/hot_numpy_sentences.npy"

with open(path, "rb") as file:
    data = np.load(file)

    # split = np.split(data, 343489)

    man = data[:343489]
    women = data[343489:]

    np.random.shuffle(man)
    np.random.shuffle(women)

    manpt1 = man[0:257616] # ca. 75%
    manpt3 = man[257616:]

    womanpt1 = women[0:251004]  # ca. 75%
    womanpt3 = women[251004:]

    print("Total man posts:" + str(len(man)))
    print("Total woman posts:" + str(len(women)))

    trainlabels = [1]*len(manpt1) + [0]*len(womanpt1)
    testinglabels = [1] * len(manpt3) + [0] * len(womanpt3)

    print(manpt1)
    print()
    print(womanpt1)
    traindata = np.concatenate([manpt1, womanpt1])
    print(len(traindata))
    testingdata= np.concatenate([manpt3, womanpt3])

    np.savez("postdatanoval", traindata=traindata, trainlabels=trainlabels,
             testingdata=testingdata, testinglabels= testinglabels)
