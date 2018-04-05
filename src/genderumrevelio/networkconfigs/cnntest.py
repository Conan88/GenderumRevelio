'''
https://ac.els-cdn.com/S1877050916326849/1-s2.0-S1877050916326849-main.pdf?_tid=53ad983e-14dc-4144-9b54-048ce6a7e42f&acdnat=1521637277_a6834ff770e8fe62aad6f00f402c76cf
'''
from __future__ import print_function

from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Embedding, Conv1D, MaxPool1D
from keras.layers import LSTM, Bidirectional, Dropout
import os

from keras import backend as K
import tensorflow as tf

def lstm_run(load_data):

    #os.environ["CUDA_VISIBLE_DEVICES"] = "0"
    #config = tf.ConfigProto()
    #config.gpu_options.allow_growth = True
    #sess = tf.Session(config = config)
    #K.set_session(sess)

    max_features = 20000
    maxlen = 200  # cut texts after this number of words (among top max_features most common words)
    batch_size = 164

    print('Loading data...')
    (x_train, y_train), (x_test, y_test) = load_data
    print(len(x_train), 'train sequences')
    print(len(x_test), 'test sequences')

    print('Pad sequences (samples x time)')
    x_train = sequence.pad_sequences(x_train, maxlen=maxlen)
    x_test = sequence.pad_sequences(x_test, maxlen=maxlen)
    print('x_train shape:', x_train.shape)
    print('x_test shape:', x_test.shape)

    print('Build model...')
    model = Sequential()
    model.add(Embedding(max_features, 128))
    model.add(Conv1D(kernel_size=30, filter=3, activation="relu"))
    model.add(MaxPool1D(pool_size=2))
    model.add(Conv1D(kernel_size=30, filter=3, activation="relu"))
    model.add(MaxPool1D(pool_size=2))
    model.add(Conv1D(kernel_size=30, filter=3, activation="relu"))
    model.add(MaxPool1D(pool_size=2))
    model.add(LSTM(30))
    model.add(Dropout(0.5))
    model.add(Dense(10, activation='tanh'))
    model.add(Dropout(0.5))
    model.add(Dense(1, activation='sigmoid'))

    # try using different optimizers and different optimizer configs
    model.compile(loss='binary_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])

    print('Train...')
    history_callback = model.fit(x_train, y_train,
              batch_size=batch_size,
              epochs=20,
              validation_data=(x_test, y_test))
    score, acc = model.evaluate(x_test, y_test,
                                batch_size=batch_size)
    print('Test score:', score)
    print('Test accuracy:', acc)

    return (history_callback.history, acc, score, model)

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
            j = json.dumps(trainingdata)
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

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import warnings
import os

def load_data(path='temp.npz', num_words=None, skip_top=0,
              maxlen=None, seed=113,
              start_char=1, oov_char=2, index_from=3, **kwargs):
    """Loads the dataset.

    # Arguments
        path: where to cache the data.
        num_words: max number of words to include. Words are ranked
            by how often they occur (in the training set) and only
            the most frequent words are kept
        skip_top: skip the top N most frequently occurring words
            (which may not be informative).
        maxlen: sequences longer than this will be filtered out.
        seed: random seed for sample shuffling.
        start_char: The start of a sequence will be marked with this character.
            Set to 1 because 0 is usually the padding character.
        oov_char: words that were cut out because of the `num_words`
            or `skip_top` limit will be replaced with this character.
        index_from: index actual words with this index and higher.

    # Returns
        Tuple of Numpy arrays: `(traindata, trainlabels), (testingdata, testlabels)`.

    # Raises
        ValueError: in case `maxlen` is so low
            that no input sequence could be kept.

    Note that the 'out of vocabulary' character is only used for
    words that were present in the training set but are not included
    because they're not making the `num_words` cut here.
    Words that were not seen in the training set but are in the test set
    have simply been skipped.
    """
    # Legacy support
    if 'nb_words' in kwargs:
        warnings.warn('The `nb_words` argument in `load_data` '
                      'has been renamed `num_words`.')
        num_words = kwargs.pop('nb_words')
    if kwargs:
        raise TypeError('Unrecognized keyword arguments: ' + str(kwargs))

    path = '../data/postdatanoval.npz'
    print(os.getcwd())
    with np.load(path) as f:
        traindata, trainlabels = f['traindata'], f['trainlabels']
        testingdata, testlabels = f['testingdata'], f['testinglabels']

    np.random.seed(seed)
    indices = np.arange(len(traindata))
    np.random.shuffle(indices)
    traindata = traindata[indices]
    trainlabels = trainlabels[indices]

    indices = np.arange(len(testingdata))
    np.random.shuffle(indices)
    testingdata = testingdata[indices]
    testlabels = testlabels[indices]


    return (traindata, trainlabels), (testingdata, testlabels)


a = lstm_run(load_data())
log(a)
