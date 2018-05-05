from keras.preprocessing.text import Tokenizer
import numpy as np
import pickle

def tokenizebooks():
    with open("menbookparagraphtextinarray.pickle", "rb") as file:
        men = pickle.load(file)
    with open("womenbookparagraphtextinarray.pickle", "rb") as file:
        women = pickle.load(file)

    print(len(men))
    print(len(women))
    t = Tokenizer(filters="<=>?@[\]^_`{|}~")
    t.fit_on_texts(men)
    t.fit_on_texts(women)
    word_index = t.word_index
    mensequences = t.texts_to_sequences(men)
    womensequences = t.texts_to_sequences(women)
    np.save("menbookparagraphtokenized", np.array(mensequences))
    np.save("womenbookparagraphtokenized", np.array(womensequences))
    with open("bookwordindex.pickle", "wb") as file:
        pickle.dump(word_index, file)    
    return(mensequences, womensequences)

def tokenizeblogs():
    with open("maleblogposttextsinarray.pickle", "rb") as file:
        men = pickle.load(file)
    with open("femaleblogposttextsinarray.pickle", "rb") as file:
        women = pickle.load(file)

    print(len(men))
    print(len(women))
    t = Tokenizer(filters="<=>?@[\]^_`{|}~")
    t.fit_on_texts(men)
    t.fit_on_texts(women)
    word_index = t.word_index
    mensequences = t.texts_to_sequences(men)
    womensequences = t.texts_to_sequences(women)
    np.save("menblogposttokenized", np.array(mensequences))
    np.save("womenblogposttokenized", np.array(womensequences))
    with open("blogwordindex.pickle", "wb") as file:
        pickle.dump(word_index, file)
    return(mensequences, womensequences)


def hi():
    print("G'day")

print("hello")

