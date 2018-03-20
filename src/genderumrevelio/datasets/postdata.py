"""Setup for data
"""
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

    path = './data/postdatanoval.npz'
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
