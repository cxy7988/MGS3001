import random


def main():
    number = random.randint(1,10)
    print("The random number is", number)
    random_five()


def random_five():
    for i in range(5):
        a = random.randint(1,1000)
        print("The random numbers is", a)


main()