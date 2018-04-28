from sklearn import GaussianNB


def run_gaussian(load_data):
    (x_train, y_train), (x_test, y_test) = load_data
    gaus = GaussianNB()
    pred = gaus.fit(x_test, y_test).predict(x_test)
    print("Number of mislabeled points out of a total %d points : %d"
        % (x_test.shape[0],(y_test != pred).sum()))
