#!/usr/bin/env python
# -*- coding: utf-8 -*-
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.text import one_hot


"""
t = Tokenizer()
encoded_data = []
stringdata = []
with open('../../../blogs/man/male_data.txt', 'r', encoding='latin-1') as f:
    for line in f:
        #stringdata.append(line)
        #data = one_hot(line, 10000)
        encoded_data.append(line)

t.fit_on_texts(encoded_data)
#enc_doc = t.texts_to_matrix(stringdata, mode='count')
print(t.word_index)
# t.sequences_to_matrix(len(stringdata), stringdata)
"""
"""
data = []
with open('../Data/test.txt', 'r', encoding='latin-1') as f:
    for line in f:
        data.append(line)

a = numpy.array(data)
numpy.save('numpy_data', a)
print(a)
"""
