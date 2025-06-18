import streamlit as st
import numpy as np
import pickle

# Load your trained model
with open('ultimate_model.pkl', 'rb') as file:
        model = pickle.load(file)

st.title("🫀 Heart Failure Risk Prediction")

st.markdown("Enter patient information to predict risk of death event.")

# Input fields
age = st.number_input("Age", min_value=0, max_value=120, value=50)
anaemia = st.selectbox("Anaemia", [0, 1])
creatinine_phosphokinase = st.number_input("Creatinine Phosphokinase", min_value=0, value=8000)
diabetes = st.selectbox("Diabetes", [0, 1])
ejection_fraction = st.slider("Ejection Fraction (%)", min_value=0, max_value=100, value=40)
high_blood_pressure = st.selectbox("High Blood Pressure", [0, 1])
platelets = st.number_input("Platelets count (kiloplatelets/mL)", min_value=10000.0, value=900000.0)
serum_creatinine = st.number_input("Serum Creatinine", min_value=0.0, value=10.0)
serum_sodium = st.number_input("Serum Sodium", min_value=100, max_value=150, value=135)
sex = st.selectbox("Sex", [0, 1])  # 0: Female, 1: Male
smoking = st.selectbox("Smoking", [0, 1])
time = st.number_input("Follow-up Period (in days)", min_value=0, value=300)

# Predict button
if st.button("Predict"):
    input_data = np.array([[age, anaemia, creatinine_phosphokinase, diabetes,
                            ejection_fraction, high_blood_pressure, platelets,
                            serum_creatinine, serum_sodium, sex, smoking, time]])
    
    prediction = model.predict(input_data)[0]
    
    if prediction == 1:
        st.error("⚠️ The model predicts a high risk of death event.")
    else:
        st.success("✅ The model predicts a low risk of death event.")

