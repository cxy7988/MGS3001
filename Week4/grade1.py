score = float(input("Enter your score: "))

if score >= 93:
    print("A")
else:
    if score >= 80:
        print("B")
    else:
        if score >=70:
            print("C")
        else:
            if score >=60:
                print("D")
            else:
                print("F")