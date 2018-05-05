import re
import os
import pickle


def getPostsFromSingleFile(filepath):

    postsfromblog = []

    try:
        with open(filepath, encoding="latin-1") as file:
            text = file.read()
            text = text.replace("\n", " ")

            # Burde ha med eller ikke?
            # text = text.replace("urlLink", "")

            m = re.findall('<post>(.*?)</post>', text)

            ant_posts = len(m)
            ant_tags = text.count("</post>")

            if ant_posts != ant_tags:
                print("Posts gotten by file " + filepath + " not consistent with </post> tags in file")
                print("posts: " + str(ant_posts))
                print("</post> tags: " + str(ant_tags))
                exit(101)

            for item in m:
                it = item.strip()
                # Replace unnecessary characters and allow special characters to stand separately to later be tokenized
                it = it.replace("\t", " ")
                it = it.replace("\r", " ")
                it = it.replace("&nbsp;", " ")
                it = it.replace(".", " . ")
                it = it.replace(",", " , ")
                it = it.replace("?", " ? ")
                it = it.replace("!", " ! ")
                it = it.replace('"', ' " ')
                it = it.replace("--", " -- ")
                it = it.replace("(", " ( ")
                it = it.replace(")", " ) ")

                # Multiple spaces to 1 space
                it = " ".join(it.split())

                if it != "":
                    postsfromblog.append(it)
    except IOError:
        print("Nope")
    # print(postsfromblog)
    print(filepath)
    return postsfromblog

def getPostsFromFolder(folderpath, savename):
    posts = []

    files = os.listdir(folderpath)

    for file in files:
        abpath = os.path.join(folderpath, file)
        if os.path.isfile(abpath):
            posts += getPostsFromSingleFile(abpath)
        else:
            print("Failed to find: " + abpath)

    print("Total posts: " + str(len(posts)))

    with open(savename, "wb") as file:
        pickle.dump(posts, file)

    print("Saved blogsposts array to: " + savename)

def blogs():
    print("Getting posts from male folder")
    getPostsFromFolder("male", "maleblogposttextsinarray.pickle")
    print("Getting posts from female folder")
    getPostsFromFolder("female", "femaleblogposttextsinarray.pickle")

def book():
    sepman = []
    try:
        with open("man.txt") as file:
            text = file.read()
            man = text.split("\n\n")
            for item in man:
                it = item.strip()
                # Replace unnecessary characters and allow special characters to stand separately to later be tokenized
                it = it.replace("\t", " ")
                it = it.replace("\r", " ")
                it = it.replace("&nbsp;", " ")
                it = it.replace(".", " . ")
                it = it.replace(",", " , ")
                it = it.replace("?", " ? ")
                it = it.replace("!", " ! ")
                it = it.replace('"', ' " ')
                it = it.replace("--", " -- ")
                it = it.replace("(", " ( ")
                it = it.replace(")", " ) ")

                # Multiple spaces to 1 space
                it = " ".join(it.split())

                if it != "":
                    sepman.append(it)

            print(len(sepman))
            with open("menbookparagraphtextinarray.pickle", "wb") as file:
                pickle.dump(sepman, file)

    except:
        print("error man")

    sepwomen = []
    try:
        with open("woman.txt") as file:
            text = file.read()
            woman = text.split("\n\n")
            for item in woman:
                it = item.strip()
                # Replace unnecessary characters and allow special characters to stand separately to later be tokenized
                it = it.replace("\t", " ")
                it = it.replace("\r", " ")
                it = it.replace("&nbsp;", " ")
                it = it.replace(".", " . ")
                it = it.replace(",", " , ")
                it = it.replace("?", " ? ")
                it = it.replace("!", " ! ")
                it = it.replace('"', ' " ')
                it = it.replace("--", " -- ")
                it = it.replace("(", " ( ")
                it = it.replace(")", " ) ")

                # Multiple spaces to 1 space
                it = " ".join(it.split())

                if it != "":
                    sepwomen.append(it)

            print(len(sepwomen))
            with open("womenbookparagraphtextinarray.pickle", "wb") as file:
                pickle.dump(sepwomen, file)

    except:
        print("error woman")



if __name__ == '__main__':
    #main()
    #getPostsFromSingleFile("C:\\Users\\Jack\\Downloads\\blogs\\male\\5114.male.25.indUnk.Scorpio.xml")
    a=1
