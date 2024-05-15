import math


def main():
    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    c = math.hypot(a,b)
    print(f"The length of the hypotenuse is: {c:.2f}")


if __name__ == '__main__':
    main()