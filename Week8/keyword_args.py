def main():
    interest_rate = float(input("Enter the interest rate: "))
    periods = float(input("Enter the number of periods: "))
    principal = float(input("Enter the principal amount: "))
    show_interest(principal, interest_rate, periods)

def show_interest(principal, rate, periods):
    interest = principal * rate * periods
    print(f"The simple interest is {interest:,.2f}")

main()