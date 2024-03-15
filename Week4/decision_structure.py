# calculate the total payment with bonus

bonus = 500
basepayment = 10000

sale =  float(input("enter your sale:"))
if sale > 50000:
    payment = basepayment + bonus
    print("Congratulations! Your bonus is $", payment+bonus)
else:
    print("Your payment is $", basepayment,"If your make sale more than 50000, you will get the bonus")