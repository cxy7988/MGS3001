def main():
    my_input()
    print("This is result:")
    my_calculation()

def my_input():
    global a
    global b
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))

def my_calculation():
    c = a + b
    print(c)

main()