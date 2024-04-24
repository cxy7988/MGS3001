def main():
    print("This program converts measurements in cups to fluid ounces.")
    cups = getCup()
    convert(cups)


def getCup():
    cups = int(input("Enter the number of cups: "))
    return cups


def convert(cups):
    ounces = cups * 8
    print("That converts to", ounces, "ounces.")


main()