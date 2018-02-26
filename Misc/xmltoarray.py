import os
import xml.etree.ElementTree as ET


def getpostsfromfile(path):
    blogposts = []

    try:
        tree = ET.parse(path)
        root = tree.getroot()
        print("a")
        for elem in root:
            # print(type(elem.tag))
            if elem.tag == "post":
                # print("post")
                blogposts.append(elem.text)
    except Exception as e:
        # print(type(e))
        print("Error!")
        with open(path, encoding="latin-1") as f:
            text = f.read()
            # print('&' in text)
            text = text.replace("&", "and")
            text = text.replace("nbsp", " ")
            text = text.replace("", " ")
            # print("&" in text)
            root = ET.fromstring(text)
            for elem in root:
                # print(type(elem.tag))
                if elem.tag == "post":
                    # print("post")
                    blogposts.append(elem.text)
    return blogposts

workingpath = "C:\\Users\\Jack\\Downloads\\blogs\\male"
files = os.listdir(workingpath)
# print(files)

count = 0
posts = []
failedfiles = []
#with open(r"C:\Users\Jack\Downloads\blogs\male\1169202.male.26.Science.Libra.xml", encoding="latin-1") as file:
 #   print(file.read())

for file in files:
    abpath = os.path.join(workingpath, file)
    if os.path.isfile(abpath):
        # print("yes")
        count += 1
        #print(abpath)
        #print(len(posts))
        posts += getpostsfromfile(abpath)
    else:
        print(os.path.join(workingpath, file))
print(count)
print(len(posts))
