import streamlit as st
import requests

API_URL = "http://localhost:8000/predict"

st.title("Insurance Premium Category Predictor")

st.markdown("Enter Details")

age = st.number_input("Your Age", min_value=1, max_value=99, value=30)
weight = st.number_input("Your Weight in Kgs", min_value=1.0, value=86.0)
height = st.number_input("Your Height in Mtr", min_value=0.5, max_value=2.5, value=1.25)
income_lpa = st.number_input("Your Income in Lakhs", min_value=0.0, value=13.25)
smoker = st.selectbox("Do You Smoke?", options=[True, False])
city = st.text_input("City", value="Mumbai")
occupation = st.selectbox("Occupation", options=['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job'])

if st.button("Predict Now"):
    input_data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation,
    }

    try:
        response = requests.post(API_URL, json=input_data)
        if response.status_code == 200:
            result = response.json()
            st.success(f"Predicted Insurance Premium Category: **{result["prediction"]}**")
        else:
            st.error(f"API Error: {response.status_code} - {response.text}")
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to API")
