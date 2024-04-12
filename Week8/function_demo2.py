import grading
def main():
    KEEP_RUNNING = "y"
    while KEEP_RUNNING == "y":
        exam1 = int(input("Enter exam1 score: "))
        exam2 = int(input("Enter exam2 score: "))
        grading.mysum(exam1, exam2)
        grading.myaver(exam1, exam2)
        grading.grade(exam1, exam2)
        KEEP_RUNNING = input("Do you want to continue? (y/n): ")


main()
