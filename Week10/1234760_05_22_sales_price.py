DISCOUNT_PERCENTAGE = 0.25


def main():
    sale_price = discount_price()
    print("The sale price is: ", sale_price)


def discount_price():
    regular_price = get_regular_price()
    sale_price = regular_price * (1 - DISCOUNT_PERCENTAGE)
    return sale_price


def get_regular_price():
    regular_price = float(input("Enter the regular price: "))
    return regular_price


main()