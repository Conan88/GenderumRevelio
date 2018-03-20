
def removelabel():
    with open("newmale.txt", "w", encoding="latin-1") as newfile:
        with open("male_data.txt", encoding="latin-1") as file:
            for line in file:
                # print(line[:-2])
                newfile.write(line[:-3] + "\n")
    with open("newfemale.txt", "w", encoding="latin-1") as newfile:
        with open("female_data.txt", encoding="latin-1") as file:
            for line in file:
                # print(line[:-2])
                newfile.write(line[:-3] + "\n")
