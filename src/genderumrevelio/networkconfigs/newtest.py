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

    os.environ["CUDA_VISIBLE_DEVICES"] = "2"
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    sess = tf.Session(config = config)
    K.set_session(sess)

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
    model.add(Conv1D(kernel_size=30, filters=2, activation="relu"))
    model.add(MaxPool1D(pool_size=2))
    model.add(Conv1D(kernel_size=30, filters=2, activation="relu"))
    model.add(MaxPool1D(pool_size=2))
    model.add(Conv1D(kernel_size=30, filters=2, activation="relu"))
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

