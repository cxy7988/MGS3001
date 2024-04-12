
def main():
    KEEP_RUNNING = "y"
    while KEEP_RUNNING == "y":
        exam1 = int(input("Enter exam1 score: "))
        exam2 = int(input("Enter exam2 score: "))
        mysum(exam1, exam2)
        myaver(exam1, exam2)
        grade(exam1, exam2)
        KEEP_RUNNING = input("Do you want to continue? (y/n): ")

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



main()
