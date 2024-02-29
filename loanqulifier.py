#loanqulifierapp.py
#This application is for test the qualification of loan

import streamlit as st
st.title("Brian's loanqulifier")
#set minimum standard
MINSALARY = 30000
MINYEAR = 5

#Get input
salary = float(st.number_input("please enter your salary:"))
year = int(st.number_input("please enter your year:"))

#Determine qualification
if st.button("Submit"):
    if salary > MINSALARY and year >  MINYEAR:
        st.write("Your application is accepted")
    else:
        st.write("Your application is rejected")
else:
    st.write("Please enter your data")

# import streamlit as st
# import numpy as np
#
# dataframe = np.random.randn(10, 20)
# st.dataframe(dataframe)