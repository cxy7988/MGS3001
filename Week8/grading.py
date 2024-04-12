def mysum(num1, num2):
    result = num1 + num2
    print("The total score is", result)


def myaver(num1, num2):
    result = (num1 + num2) / 2
    print("The average is", result)

def grade(num1, num2):
    average = (num1 + num2) / 2
    if average >= 93:
        print("A")
    elif average >= 90:
        print("B")
    else:
        print("F")

