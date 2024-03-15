import streamlit as st
st.title("Loan Qulifier")


mininum_salary = 50000
minimun_work_year = 3

salary = float(st.number_input("Enter your salary: "))
work_year = int(st.number_input("Enter your work year: "))

if st.bottom("summit"):
    if mininum_salary <= salary and work_year >= minimun_work_year:
        st.write("Your application has been proved")
    else:
        st.write("Sorry, your application has been rejected")