import json

path = "unfilteredtweets/"

def checker(name):
    print("unfiltered")
    with open(path + name + ".json", "r") as file:
        data = json.load(file)
        count = 0
        for i in range(0, len(data)):
            if data[i]["user"].lower() == name:
                count += 1

        print("total: " + str(len(data)))
        print("correct: " + str(count))

    print("filtered")
    with open("../unfilteredtweets/" + name + ".json", "r") as file:
        data = json.load(file)
        count = 0
        for i in range(0, len(data)):
            if data[i]["user"].lower() == name:
                count += 1

        print("total: " + str(len(data)))
        print("correct: " + str(count))
        print()


def main():
    with open("users.txt", "r") as f:
        for line in f:
            if line.strip() != "":
                print(line.strip())
                checker(line.strip())

if __name__ == '__main__':
    with open(r"C:\Users\Jack\Downloads\blogs\male\1005545.male.25.Engineering.Sagittarius.xml", encoding="latin-1") as file:
        file.read()
    with open(r"C:\Users\Jack\Downloads\blogs\male\1004904.male.23.Arts.Capricorn.xml", encoding="latin-1") as file:
        file.read()
    with open(r"C:\Users\Jack\Downloads\blogs\male\1169202.male.26.Science.Libra.xml", encoding="latin-1") as file:
        text = file.read()
        text = text.replace("&", "and")
        text = text.replace("nbsp", " ")
        #text = text.replace("", " ")
        print(text)

    import locale
    print(locale.getpreferredencoding())
