def main():
    f_list = open("friendlist.txt","r")
    line1 = f_list.readline()
    line2 = f_list.readline()
    line3 = f_list.readline()
    line1 = line1.rstrip("\n")
    line2 = line2.rstrip("\n")
    line3 = line3.rstrip("\n")
    f_list.close()
    print(line1)
    print(line2)
    print(line3)