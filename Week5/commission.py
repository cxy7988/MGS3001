keep_doing = "y"
while keep_doing == "y":
    commission_rate = float(input("enter commission rate: "))
    sales = float(input("enter sales: "))
    commission = commission_rate * sales
    print(f"your commission is ${commission:.2f}")
    keep_doing = input("Do you want calculate another commission? (y/n):")
print("Goodbye!")
