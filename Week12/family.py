def main():
    write()
    read()
    readline()


def write():
    familylist = open("familylist.txt", "w")
    familylist.write("Mother\n")
    familylist.write("Father\n")
    familylist.write("Sister\n")
    familylist.write("Brother\n")
    familylist.close()


def read():
    famliylist = open("familylist.txt", "r")
    family_name = famliylist.read()
    famliylist.close()
    print(family_name)


def readline():
    familylist = open("familylist.txt", "r")
    for i in range(4):
        family_name = familylist.readline()
        print(family_name)
    familylist.close()



main()