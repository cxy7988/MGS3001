proceed = "y"
MARK_UP = 0.025

while proceed == "y" or proceed == "Y" :
    wholesale_cost = float(input("input your wholesale cost: "))
    margin = wholesale_cost * MARK_UP
    retail = wholesale_cost + margin
    while wholesale_cost < 0:
        print("error input")
        wholesale_cost = float(input("input your wholesale cost: "))
    print(f"whole the wholesale cost is {wholesale_cost:,2f}, your margin is {margin:,2f},and your retail is {retail:,2f}")
    proceed = str(input("Do you want to continue? (y/n): "))


