import streamlit as st

st.title("Test Score Average Calculator")

student_number = st.number_input("Enter student number:", min_value=1, value=1, step=1)
test_number = st.number_input("Enter number of tests:", min_value=1, value=1, step=1)

# Initialize a session state variable to store scores
st.session_state['scores'] = [[0.0]*test_number for _ in range(student_number)]

# Dynamically generate score inputs
for i in range(student_number):
    for t in range(test_number):
        score_input = st.number_input(f"Enter student {i + 1} test {t + 1} score:", key=f"score_{i}_{t}", min_value=0.0,max_value=100.0)
        st.session_state.scores[i][t] = score_input

# Calculate and display averages button
if st.button("Calculate Averages"):
    score_all = 0
    for i in range(student_number):
        student_scores = st.session_state.scores[i]
        average_score = sum(student_scores) / test_number
        score_all += sum(student_scores)
        st.write(f"The average score of student {i + 1} is {average_score}")

    # Calculate total class average
    class_average = score_all / (student_number * test_number)
    st.write(f"The total average score of all tests in class is {class_average}")