import xml.etree.ElementTree as ET

# XML formated
# path = "C:\\Users\\Jack\\Downloads\\blogs\\male\\3529877.male.23.indUnk.Virgo.xml"

# Not XML formated
path = "C:\\Users\\Jack\\Downloads\\blogs\\male\\5114.male.25.indUnk.Scorpio.xml"

posts = []

try:
    tree = ET.parse(path)
    root = tree.getroot()
    for elem in root:
        # print(type(elem.tag))
        if elem.tag == "post":
            print("post")
            posts.append(elem.text)
        else:
            print("other")
except Exception as e:
    # print(type(e))
    # print("Error!")
    with open(path, 'r') as file:
        text = file.read()
        # print('&' in text)
        text = text.replace("&", "and")
        # print("&" in text)
        root = ET.fromstring(text)
        for elem in root:
            # print(type(elem.tag))
            if elem.tag == "post":
                print("post")
                posts.append(elem.text)
            else:
                print("other")
print(len(posts))
print(posts[0])
