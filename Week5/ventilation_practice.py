import streamlit as st
proceed = "y"


while proceed == "y":
    score = float(st.number_input("Enter your score: "))
    while score < 0 or score > 100:
        st.write("Error, the score must be positive")
        score = float(st.number_input("Enter your score: "))
    if st.button("exit"):
        exit()
