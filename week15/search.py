def main():
    found = False
    coffee = open("coffee.txt","r")
    search = input("Which coffee do you want to search")
    descr = coffee.readline()

    while descr != "":
        qua = float(coffee.readline())
        descr = descr.rstrip("\n")
        if search == descr:
            print("--The item's details are the following--")
            print(f"Description is {descr}")
            print(f"Quantity is {qua}")
            found = True
        descr = coffee.readline()
    coffee.close()

    if not found:
        print("The coffee is not be found")

main()