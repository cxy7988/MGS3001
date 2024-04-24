def main():
    firstname()
    lastname()
    reverse_name()

def firstname():
    global firstname
    firstname = input("Enter your first name: ")

def lastname():
    global lastname
    lastname = input("Enter your last name: ")

def reverse_name():
    print("Your name in reverse is", lastname, firstname)

main()
