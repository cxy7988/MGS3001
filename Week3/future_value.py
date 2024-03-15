# to get a number of future value


import streamlit as st

st.title("Future Value caculation")
desired_FV = float(st.number.input("Enter the desired FV here"))
interest_rate = float(st.number.input("Enter the interest rate here"))
years = int(st.number.input("Enter the number of years"))



if st.button("Calculate"):
    present_value = desired_FV / (1 + interest_rate) ** years
    print(f"The present value shoule be {present_value:,.2f}")
else:
    st.write("Please enter information")