# calculate the total payment with bonus
import streamlit as st
st.title("Payment App")

bonus = 500
basepayment = 10000

sale =  float(st.number_input("enter your sale:"))

if st.button("Submit"):
    if sale > 50000:
        payment = basepayment + bonus
        st.write("Congratulations! Your bonus is $", bonus, "so your total payment is $", payment)
    else:
        st.write("Your payment is $", basepayment,"If your make sale more than 50000, you will get the bonus")