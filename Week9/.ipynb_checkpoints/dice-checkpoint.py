import random
MIN = 1
MAX = 6


def main():
    print("Rolling the dice...")
    print("First computer roll")
    print("Hit enter to roll the dice")
    input("")
    comdice = roll_dice()
    print("It is your turn to roll the dice")
    input("")
    youdice = roll_dice()
    who_won(comdice, youdice)


def roll_dice():
    die1 = random.randint(MIN, MAX)
    print("The values are:", die1)
    return die1


def who_won(com, you):
    if com > you:
        print("Computer wins")
    elif com < you:
        print("You win")
    else:
        print("It is a tie")

main()
