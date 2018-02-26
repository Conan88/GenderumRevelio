#!/usr/bin/env python
# -*- coding: utf-8 -*-
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.text import text_to_word_sequence
from keras.preprocessing.text import hashing_trick


t = Tokenizer()
tt = text_to_word_sequence
ttt = hashing_trick

encoded_data = []
with open('../Data/test.txt', 'r', encoding='latin-1') as f:
    for line in f:
        data = ttt(line, 100)
        print(data)
