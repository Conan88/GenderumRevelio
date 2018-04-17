"""Setup for data
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import warnings
import os


def load_data(path):
    with open(path, "rb") as f:
        data = np.load(f)
        np.random.shuffle(data)
    return data

def load_blogs(datacut=1, datasplit=0.75, load_dataset='book', activation='sigmoid', seed=113, **kwargs):
    # TODO: add datacut and datasplit to input
    # Path's to numpy files
    if load_dataset == 'book':
        man_data_path = './data/bookdata/menbookparagraphtokenized.npy'
        woman_data_path = './data/bookdata/womenbookparagraphtokenized.npy'
    if load_dataset == 'blog':
        man_data_path = './data/blogdata/menblogposttokenized.npy'
        woman_data_path = './data/blogdata/womenblogposttokenized.npy'

    # Load the data and shuffle it
    man = load_data(man_data_path)
    woman = load_data(woman_data_path)

    #TODO: check for division by 0 error
#    assert(datacut = 0, "Division by 0 is not good!"i)
    if datacut != 1:
        for i in range(int(len(man) * datacut)):
            man = man[1:]
        for i in range(int(len(woman) * datacut)):
            woman = woman[1:]
    # Split data 75% training data
    training_data_man = man[0:int(len(man) * datasplit)]
    training_data_woman = woman[0:int(len(woman) * datasplit)]

    # Split 25% validation data
    test_data_man = man[int(len(man) * datasplit):]
    test_data_woman = woman[int(len(woman) * datasplit):]

    # Create labels
    if activation == 'sigmoid':
        training_data_labels = np.array([1] * len(training_data_man) + [0] * len(training_data_woman))
        test_data_labels = np.array([1] * len(test_data_man) + [0] * len(test_data_woman))
    if activation == 'softmax':
        training_data_labels = np.array([[1,0]] * len(training_data_man) + [[0,1]] * len(training_data_woman))
        test_data_labels = np.array([[1,0]] * len(test_data_man) + [[0,1]] * len(test_data_woman))

    # Create data lists
    training_data = np.concatenate([training_data_man, training_data_woman])
    test_data = np.concatenate([test_data_man, test_data_woman])

    np.random.seed(seed)
    print("lengths")
    print(len(training_data))
    print(len(training_data))
    indices = np.arange(len(training_data))
    print("types")
    print(type(indices))
    print(type(training_data_labels))
    np.random.shuffle(indices)
    training_data = training_data[indices]
    training_data_labels = training_data_labels[indices]

    indices = np.arange(len(test_data))
    np.random.shuffle(indices)
    test_data = test_data[indices]
    test_data_labels = test_data_labels[indices]
    return (training_data, training_data_labels), (test_data, test_data_labels)
