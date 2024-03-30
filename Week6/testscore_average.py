student_number = int(input("Enter student number: "))
test_number = int(input("Enter times of test: "))

for i in range(1,student_number+1):
    print("student number ", i)
    print("---------------")
    score_total = 0
    for t in range(1,test_number+1):
        score = float(input(f"Enter student {i} test {t} score here: "))
        score_total = score_total + score
    score_average = score_total / test_number
    print(f"The average score of student {i} is {score_average}")
    print("")