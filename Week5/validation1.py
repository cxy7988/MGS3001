score = float(input("Enter your score: "))
while score < 0 or score > 100:
    print("Error, the score must be positive")
    score = float(input("Enter your score: "))
print("Thanks")