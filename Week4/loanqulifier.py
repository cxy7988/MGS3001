import streamlit as st


mininum_salary = 50000
minimun_work_year = 3

salary = float(input("Enter your salary: "))
work_year = int(input("Enter your work year: "))

if mininum_salary <= salary and work_year >= minimun_work_year:
    print("Your application has been proved")
else:
    print("Sorry, your application has been rejected")