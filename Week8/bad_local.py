def main():
    get_name()
    print("Hello", name)


def get_name():
    global name
    name = input("Enter your name: ")


main()
