import re
import os
import pickle


def getposts(path):

    postsfromblog = []

    try:
        with open(path, encoding="latin-1") as file:
            text = file.read()
            text = text.replace("\n", "")
            text = text.replace("\t", "")
            text = text.replace("\r", "")
            text = text.replace("&nbsp;", " ")
            # Burde ha med eller ikke?
            # text = text.replace("urlLink", "")

            m = re.findall('<post>(.*?)</post>', text)

            ant_posts = len(m)
            ant_tags = text.count("</post>")

            if ant_posts != ant_tags:
                print("Posts gotten by file not consistent with </post> tags in file")
                print("posts:" + str(ant_posts))
                print("</post> tags: " + str(ant_tags))
                exit(101)

            for item in m:
                it = item.strip()
                if it != "":
                    postsfromblog.append(it)
    except IOError:
        print("Nope")

    return postsfromblog


def main():

    posts = []

    workingpath = "C:\\Users\\Jack\\Downloads\\blogs\\male"
    files = os.listdir(workingpath)

    for file in files:
        abpath = os.path.join(workingpath, file)
        if os.path.isfile(abpath):
            posts += getposts(abpath)

    print("Total male posts: " + str(len(posts)))
    print("Done with male blogs")

    with open("male.pickle", "wb") as file:
        pickle.dump(posts, file)

    print("Saved male blogs array")

    posts = []

    workingpath = "C:\\Users\\Jack\\Downloads\\blogs\\female"
    files = os.listdir(workingpath)

    for file in files:
        abpath = os.path.join(workingpath, file)
        if os.path.isfile(abpath):
            posts += getposts(abpath)

    print("Total female posts: " + str(len(posts)))
    print("Done with female blogs")

    with open("female.pickle", "wb") as file:
        pickle.dump(posts, file)

    print("Saved female blogs array")


if __name__ == '__main__':
    main()
    # getposts("fjdsaklfjda")
