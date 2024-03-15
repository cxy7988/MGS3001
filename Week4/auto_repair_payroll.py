basehours = 40
multiplier = 1.5

hours = int(input("How many hours do you work in weeks"))
pay_rate = float(input("enter your pay rate(how much yun per hour)"))

if hours >= basehours:
    payroll = ((hours - basehours) * multiplier + basehours) * pay_rate
    print(f"You work {hours} hours this week, your total payment is {payroll:.2f}")
else:
    payroll = hours * pay_rate
    print(f"your total payment is {payroll:.2f}")