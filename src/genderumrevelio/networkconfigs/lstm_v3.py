
'''Trains an LSTM model on the IMDB sentiment classification task.

The dataset is actually too small for LSTM to be of any advantage
compared to simpler, much faster methods such as TF-IDF + LogReg.

# Notes

- RNNs are tricky. Choice of batch size is important,
choice of loss and optimizer is critical, etc.
Some configurations won't converge.

- LSTM loss decrease patterns during training can be quite different
from what you see with CNNs/MLPs/etc.
'''
from __future__ import print_function

from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Embedding
from keras.layers import LSTM, Bidirectional, Dropout
import os

from keras import backend as K
import tensorflow as tf
from keras import optimizers

def get_loadinfo():
    #datacut=1, datacut=0.75, load_dataset="book", activcation='sigmoid', seed=113, **kwargs
    return (1, 0.5, "book", "sigmoid")


def lstm_run(load_data):

    os.environ["CUDA_VISIBLE_DEVICES"] = "1"
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    sess = tf.Session(config = config)
    K.set_session(sess)

    max_features = 20000
    maxlen = 1200  # cut texts after this number of words (among top max_features most common words)
    batch_size = 32

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
    model.add(Embedding(max_features, 50))
    model.add(Bidirectional(LSTM(50)))
    model.add(Dropout(0.3))
    model.add(Dense(20, activation='relu'))
    model.add(Dense(40, activation='relu'))
    model.add(Dense(30, activation='relu'))
    model.add(Dense(5, activation='relu'))
    model.add(Dropout(0.3))
    model.add(Dense(1, activation='sigmoid'))
    #model.add(tf.keras.backend.round(Dense(1, activation='sigmoid')))

    adam = optimizers.Adam(lr=0.01)
    # try using different optimizers and different optimizer configs
    model.compile(loss='binary_crossentropy',
                  optimizer=adam,
                  metrics=['accuracy'])

    print('Train...')
    history_callback = model.fit(x_train, y_train,
              batch_size=batch_size,
              epochs=10,
              validation_data=(x_test, y_test))
    score, acc = model.evaluate(x_test, y_test,
                                batch_size=batch_size)
    print('Test score:', score)
    print('Test accuracy:', acc)

    return (history_callback.history, acc, score, model, os.path.abspath(__file__))
