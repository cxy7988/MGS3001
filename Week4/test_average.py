score1 = float(input('Enter score1: '))
score2 = float(input('Enter score2: '))
score3 = float(input('Enter score3: '))
average = (score1 + score2 + score3) / 3
if average >= 93:
    print("Your average score is",average,"Congratulation!")
else:
    print("Your average is not enough, study hard in next exam")
