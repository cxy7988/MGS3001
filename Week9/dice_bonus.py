import random
MIN = 1
MAX = 6


def main():
    proceed = "y"
    while proceed == "y":
        score = 0
        for i in range(5):
            print("Rolling the dice...")
            print("First computer roll")
            print("Hit enter to roll the dice")
            input("")
            comdice = roll_dice()
            print("It is your turn to roll the dice")
            input("")
            youdice = roll_dice()
            score = score + who_won(comdice, youdice)
        proceed = final_won(score)


def roll_dice():
    die = random.randint(MIN, MAX)
    print("The values are:", die)
    return die


def who_won(com, you):
    if com > you:
        print("Computer wins")
        a = -1
    elif com < you:
        print("You win")
        a = 1
    else:
        print("It is a tie")
        a = 0
    return a


def final_won(score):
    if score > 0:
        print("You win the game")
        proceeds = "n"
    elif score < 0:
        print("Computer wins the game")
        proceeds = "n"
    else:
        print("It is a tie,do you want to play again?,y/n")
        proceeds = input("")
    return proceeds

main()

