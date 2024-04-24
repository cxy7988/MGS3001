def main():
    gross_pay = float(input("Enter your gross pay: "))
    bonus = float(input("Enter your bonus: "))
    pay = show_pay_contributions(gross_pay,bonus)
    show_bonus_contributions(pay)


def show_pay_contributions(amount1, amount2):
    pay = amount1 + amount2
    print("The pay contribution is", pay)
    return pay


def show_bonus_contributions(amount):
    bonus = amount * 0.05
    print("The bonus contribution is", bonus)

main()