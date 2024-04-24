import random

head = 1
tail = 2
tosses = int(input("Enter the number of coin tosses: "))


def main(time):
    heads = 0
    tails = 0
    for i in range(time):
        if random.randint(head, tail) == head:
            #print("Heads")
            heads = heads + 1
        else:
            #print("No head")
            tails = tails + 1
    print("Number of heads: ", heads)
    print("Number of tails: ", tails)
    print(f"The probability of heads is: {heads/time:.2f}")
    print(f"The probability of tails is: {tails/time:.2f}")


if __name__ == '__main__':
    main(tosses)