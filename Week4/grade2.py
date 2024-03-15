score = float(input("Enter your score: "))


if score >= 93:
    print("A")
    print(f"your grade is {score},you need much {(93-score/2)*2} more score to get A")
elif score >=80:
    print("B")
    print(f"your grade is {score},you need much {(93-score/2)*2} more score to get A")
elif score >=70:
    print("C")
    print(f"your grade is {score},you need much {(93-score/2)*2} more score to get A")
elif score >=60:
    print("D")
    print(f"your grade is {score},you need much {(93-score/2)*2} more score to get A")
else:
    print("F")
    print(f"your grade is {score},you need much {(93-score/2)*2} more score to get A")