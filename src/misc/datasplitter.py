import numpy as np

path = r"../data/hot_numpy_posts.npy"

with open(path, "rb") as file:
    data = np.load(file)

    # split = np.split(data, 343489)

    man = data[:343489]
    women = data[343489:]

    np.random.shuffle(man)
    np.random.shuffle(women)

    manpt1 = man[0:171744] # nesten 50%
    manpt2 = man[171744:257616] # ca. 25%
    manpt3 = man[257616:] # sammsies

    womanpt1 = women[0:167336]  # nesten 50%
    womanpt2 = women[167336:251004]  # ca. 25%
    womanpt3 = women[251004:]  # sammsies

    print("Total man posts:" + str(len(man)))
    print("Total woman posts:" + str(len(women)))

    trainlabels = [1]*len(manpt1) + [0]*len(womanpt1)
    validationlabels = [1] * len(manpt2) + [0] * len(womanpt2)
    testinglabels = [1] * len(manpt3) + [0] * len(womanpt3)

    print(manpt1)
    print()
    print(womanpt1)
    traindata = np.concatenate([manpt1, womanpt1])
    print(len(traindata))
    validationdata = np.concatenate([manpt2, womanpt2])
    testingdata= np.concatenate([manpt3, womanpt3])

    np.savez("postdata", traindata=traindata, trainlabels=trainlabels, validationdata=validationdata, validationlabels=validationlabels,
             testingdata=testingdata, testinglabels= testinglabels)
