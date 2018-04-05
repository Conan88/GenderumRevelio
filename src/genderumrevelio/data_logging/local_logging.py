import json
import os
import time
import datetime
import matplotlib.pyplot as pl
import pandas as pd
import shutil


def log(log):
    """Getting the data from keras"""
    trainingdata = log[0]
    final_acc = log[1]
    score = log[2]
    model = log[3]

    try:
        if not os.path.isdir("../data"):
            os.makedirs("../data")
    except:
        print("Failed to create ../data folder")

    try:
        if not os.path.isdir("../data/logs"):
            os.makedirs("../data/logs")
    except:
        print("Failed to create ../data/logs folder")

    i = 1
    prename = "../data/logs/network"

    while os.path.isdir(prename + str(i)):
        i += 1
    path = prename + str(i)
    os.mkdir(path)

    # Save data on loss and accuracy for each epoch
    try:
        with open(os.path.join(path, "callback.json"), "w") as file:
            j = json.dumps(trainingdata, indent=4, sort_keys=True)
            file.write(j)
        print("Saved callback history")
    except:
        print("Failed save callback")

    # Save plot of epoch data
    try:
        df = pd.DataFrame(trainingdata)
        df.plot()
        pl.savefig(os.path.join(path, "epoch.png"))
        print("Saved pyplot of callback info")
    except:
        print("Failed to save pyplot of callback info")

    # Save the actual file/setting (i.e. a copy of this script)
    try:
        shutil.copy(__file__, os.path.join(path, os.path.basename(__file__)))
        "Copied file"
    except:
        print("Failed to copy source file")

    # Save the test accuracy and test score
    try:
        with open(os.path.join(path, "results.txt"), "w") as file:
            file.write(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
            file.write('Test score: ' + str(score) + "\n")
            file.write('Test accuracy: ' + str(final_acc) + "\n")
        print("Saved test results")
    except:
        print("Failed to save test results")

    try:
        model.save(os.path.join(path, "my_model.h5"))
        print("Saved model")
    except:
        print("Failed to save model")
