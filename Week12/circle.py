import math


def main():
    radius = float(input("Enter the radius of the circle: "))
    print("The circum of the circle is",circum(radius))
    print("The area of the circle is",area(radius))


def circum(radius):
    circum = 2 * math.pi * radius
    return circum


def area(radius):
    area = math.pi * radius ** 2
    return area


main()
