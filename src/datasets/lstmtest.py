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
from keras.layers import LSTM, Bidirectional
from postdata import load_data
import shutil
import json
import os
import time
import datetime

max_features = 20000
maxlen = 80  # cut texts after this number of words (among top max_features most common words)
batch_size = 124

print('Loading data...')
(x_train, y_train), (x_test, y_test) = load_data()
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
model.add(Bidirectional(LSTM(128, dropout=0.2, recurrent_dropout=0.2)))
model.add(Dense(100, activation='relu'))
model.add(Dense(50, activation='relu'))
model.add(Dense(2, activation='sigmoid'))

# try using different optimizers and different optimizer configs
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

print('Train...')
history_callback = model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=50,
          validation_data=(x_test, y_test))
score, acc = model.evaluate(x_test, y_test,
                            batch_size=batch_size)
print('Test score:', score)
print('Test accuracy:', acc)

i = 1
prename = "network"

while os.path.isdir(prename + str(i)):
    i += 1
path = prename + str(i)
os.mkdir(path)

# Save data on loss and accuracy for each epoch
with open(os.path.join(path, "callback.json"), "w") as file:
    j = json.dumps(history_callback.history)
    file.write(j)
print(history_callback.history)
print("Saved callback history")

# Save the actual file/setting (i.e. a copy of this script)
shutil.copy(__file__, os.path.join(path, os.path.basename(__file__)))
"Copied file"

# Save the test accuracy and test score
with open(os.path.join(path, "results.txt"), "w") as file:
    file.write(st=datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
    file.write('Test score: ' + str(score) + "\n")
    file.write('Test accuracy: ' + str(acc) + "\n")
print("Saved test results")

model.save(os.path.join(path, "my_model.h5"))
print("Saved model")