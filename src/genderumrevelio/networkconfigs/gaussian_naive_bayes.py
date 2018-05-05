from sklearn.naive_bayes import GaussianNB
import numpy as np
from keras.preprocessing.sequence import pad_sequences


def run_gaussian(load_data):
    (x_train, y_train), (x_test, y_test) = load_data
    train_test = x_test
    new_list = []
    for i in range(0, len(train_test)):
       new_list.append(np.array(train_test[i]))
    new_list = np.array(new_list)
    train_test = new_list
    train_test = pad_sequences(train_test)
    gaus = GaussianNB()
    pred = gaus.fit(train_test, y_test).predict(train_test)
    print("Number of mislabeled points out of a total %d points : %d"
        % (train_test.shape[0],(y_test != pred).sum()))
    a = train_test.shape[0]
    b = (y_test != pred).sum()
    print("Acc precent: %d" % (float(b)/float(a)*100.0))


def testing(load_data):
    (x_train, y_train), (x_test, y_test) = load_data
    print("type is: ",type(x_test[0]))
    new_list = []
    for i in range(0, len(x_test)):
       new_list.append(np.array(x_test[i]))
    new_list = np.array(new_list)
    print(new_list[0])
    print("type of newlist: ",type(new_list))
    print("type of newlist item: ",type(new_list[0]))
