print(f"Brian is handsome")
name = "Brian"
print(f"Hello {name}")
print(f"the value is {10+2}")
num=2.647286
print(f"The value is {num:.2f}")
print(f"The value is {num:.3f}")
print(f"The value is {num:.4f}")
discount = 0.5
print(f"The discount is {discount:.0%}")

#alignment
print(f"{num:<20.2f}")
print(f"{num:>20.2f}")
print(f"{num:^20.2f}")
print(f"{num:<40.2f}")
print(f"{num:>40.2f}")
print(f"{num:^40.2f}")

m_payment = 5000.45
a_payment = m_payment * 12
print(f"{a_payment:<30.2f}")
print(f"{a_payment:>30.2f}")
print(f"{a_payment:^30.2f}")

exit()