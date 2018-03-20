import re
import os


workingpath = "C:\\Users\\Jack\\Downloads\\blogs\\male"
files = os.listdir(workingpath)
# print(files)

count = 0
posts = []
failedfiles = []
with open(r"C:\Users\Jack\Downloads\blogs\male\1169202.male.26.Science.Libra.xml", encoding="latin-1") as file:
    text = file.read()
    m = re.findall('<post>(.*)</post>', text)
    print(text)
    print(len(m))

"""
for file in files:
    abpath = os.path.join(workingpath, file)
    if os.path.isfile(abpath):
        print("yes")
        count += 1
        #print(abpath)
        #print(len(posts))
        with open(abpath, encoding="latin-1") as file:
            text = file.read()
            print(text)
    else:
        print(os.path.join(workingpath, file))
print(count)
print(len(posts))
"""