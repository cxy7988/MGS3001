def main1():
    infile = open("coffee.txt","r")
    for line in infile:
        line = line.rstrip("\n")
        print(line)


def main2():
    infile = open("coffee.txt", "r")
    des = infile.readline()
    while des !="":
        qty = float(infile.readline())
        des = des.rstrip("\n")
        print(f"The description is {des}")
        print(f"The quantity is {qty}")
        des = infile.readline()

main2()
