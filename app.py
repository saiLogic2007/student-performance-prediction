import streamlit as st
import pickle
import pandas as pd




with open("student_model.pkl", "rb") as file:
    model = pickle.load(file)

with open("label_encoder.pkl", "rb") as file:
    encoder = pickle.load(file)




st.set_page_config(
    page_title="Student Performance Prediction",
    page_icon="🎓",
    layout="centered"
)


st.title("🎓 Student Performance Prediction System")

st.write(
    "Enter the student's academic details to predict performance."
)




name = st.text_input("Student Name")

attendance = st.number_input(
    "Attendance (%)",
    min_value=0.0,
    max_value=100.0,
    value=75.0
)

internal_marks = st.number_input(
    "Internal Marks",
    min_value=0.0,
    max_value=100.0,
    value=60.0
)

study_hours = st.number_input(
    "Study Hours / Day",
    min_value=0.0,
    value=3.0
)

previous_marks = st.number_input(
    "Previous Marks",
    min_value=0.0,
    max_value=100.0,
    value=60.0
)

assignment_marks = st.number_input(
    "Assignment Marks",
    min_value=0.0,
    max_value=100.0,
    value=60.0
)

backlogs = st.number_input(
    "Number of Backlogs",
    min_value=0,
    step=1
)


if st.button("🔮 Predict Performance"):

    if name.strip() == "":
        st.error("Please enter the student's name.")

    else:

        student_data = [[
            attendance,
            internal_marks,
            study_hours,
            previous_marks,
            assignment_marks,
            backlogs
        ]]


        prediction = model.predict(student_data)

        result = encoder.inverse_transform(prediction)[0]

        st.divider()


        if result == "Good":

            st.success(
                f"### ✅ GOOD PERFORMANCE\n\n"
                f"Student: **{name}**"
            )

            st.info(
                "📊 **Performance Status: ON TRACK**"
            )



        else:

            st.error(
                f"### ⚠️ POOR PERFORMANCE\n\n"
                f"Student: **{name}**"
            )

            st.warning(
                "📊 **Performance Status: NEEDS IMPROVEMENT**"
            )

          
