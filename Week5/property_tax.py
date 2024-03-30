proceed = 1
tax_rate = 0.0065
while proceed != 0:
    value = float(input("enter your value:"))
    tax = value * tax_rate
    print("your tax is",tax)
    proceed = int(input("if you want to exit, please input 0"))
