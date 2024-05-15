import geometey_import


def main():
    choose = int(input("Enter your choice here,\n 1 for circle circumference,\n 2 for circle area,"
                       "\n 3 for rectangle permenter,\n 4 for rectangle area,\n 5 to exit: "))
    if choose == 1:
        radius = float(input("Enter the radius of the circle: "))
        print("The circum of the circle is", geometey_import.circum(radius))
    elif choose == 2:
        radius = float(input("Enter the radius of the circle: "))
        print("The area of the circle is", geometey_import.circle_area(radius))
    elif choose == 3:
        weight = float(input("Enter the weight of the package: "))
        height = float(input("Enter the height of the package: "))
        print("The perimeter of the circle is", geometey_import.peri(weight, height))
    elif choose == 4:
        weight = float(input("Enter the weight of the package: "))
        height = float(input("Enter the height of the package: "))
        print("The area of the circle is", geometey_import.rectanggle_area(weight, height))
    elif choose == 5:
        print("Exiting the program")
    else:
        print("Invalid input")

main()