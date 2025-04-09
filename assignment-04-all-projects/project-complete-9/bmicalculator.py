# Streamlit BMI Calculator 🧮

import streamlit as st

st.title("BMI Calculator")

height = st.number_input("Enter your height (in meters):")
weight = st.number_input("Enter your weight (in kg):")

if height > 0 and weight > 0:
    bmi = weight / (height ** 2)
    st.write("Your BMI is:", round(bmi, 2))

    if bmi < 18.5:
        st.warning("Underweight")
    elif 18.5 <= bmi < 24.9:
        st.success("Normal weight")
    elif 25 <= bmi < 29.9:
        st.info("Overweight")
    else:
        st.error("Obese")