import numpy as np


def infodata():

    path = "postdatanoval.npz"

    with np.load(path) as f:
        traindata, trainlabels = f['traindata'], f['trainlabels']
        testingdata, testlabels = f['testingdata'], f['testinglabels']

        print(trainlabels[1])
        print(trainlabels[100])
        print(trainlabels[-100])
        print(trainlabels[-1])

        print(type(testlabels))


def arraylabel():

    path = r"../data/hot_numpy_posts.npy"

    with open(path, "rb") as file:
        data = np.load(file)

        # split = np.split(data, 343489)

        man = data[:343489]
        women = data[343489:]

        np.random.shuffle(man)
        np.random.shuffle(women)

        manpt1 = man[0:257616]  # ca. 75%
        manpt3 = man[257616:]

        womanpt1 = women[0:251004]  # ca. 75%
        womanpt3 = women[251004:]

        print("Total man posts:" + str(len(man)))
        print("Total woman posts:" + str(len(women)))

        trainlabels = [[1, 0]] * len(manpt1) + [[0, 1]] * len(womanpt1)
        testinglabels = [[1, 0]] * len(manpt3) + [[0, 1]] * len(womanpt3)

        # print(manpt1)
        print()
        # print(womanpt1)
        traindata = np.concatenate([manpt1, womanpt1])
        print(len(traindata))
        testingdata = np.concatenate([manpt3, womanpt3])

        np.savez("postdatasoftmax", traindata=traindata, trainlabels=trainlabels,
                 testingdata=testingdata, testinglabels=testinglabels)


def postsplit():

    print(1)
