def main():
    weight = float(input("Enter the weight of the package: "))
    height = float(input("Enter the height of the package: "))
    print("The perimeter of the circle is",peri(weight, height))
    print("The area of the circle is",area(weight, height))


def peri(weight, height):
    peri1 = 2*(weight + height)
    return peri1


def area(weight, height):
    area1 = weight * height
    return area1


main()