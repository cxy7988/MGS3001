def main():
    sales = float(input("Enter the sales amount: "))
    advanced_pay = get_advanced_pay()
    commission_rate = get_commission_rate(sales)
    commission = sales * commission_rate - advanced_pay
    print(f"This month sale was: {sales:,.2f}, and the advanced pay was: {advanced_pay:,.2f}")
    print(f"The commission is: {commission:,.2f}")


def get_advanced_pay():
    advanced_pay = float(input("Enter the advanced pay amount: "))
    return advanced_pay


def get_commission_rate(sales):
    if sales <= 10000:
        return 0.10
    elif sales <= 14999.99:
        return 0.12
    elif sales <= 17999.99:
        return 0.14
    elif sales <= 21999.99:
        return 0.16
    else:
        return 0.18

main()