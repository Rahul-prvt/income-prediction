import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load the trained Decision Tree model from the notebook
dt_model = joblib.load("DecisionTreeClas.pkl")

# Load LabelEncoders from the notebook
enconders = {
    "education": joblib.load("education_encoder.pkl"),
    "marital-status": joblib.load("marital_status_encoder.pkl"),
    "occupation": joblib.load("occupation_encoder.pkl"),
    "relationship": joblib.load("relationship_encoder.pkl"),
    "native-country": joblib.load("native_country_encoder.pkl"),
    "sex": joblib.load("sex_encoder.pkl"),
    "workclass": joblib.load("work_class_encoder.pkl"),
}

# Streamlit UI
st.title("Income Prediction App")
st.write("Enter the details below to predict if you are RICH  or NOT ")

# Collect user inputs
education = st.selectbox("Education", enconders["education"].classes_)
marital_status = st.selectbox("Marital Status", enconders["marital-status"].classes_)
occupation = st.selectbox("Occupation", enconders["occupation"].classes_)
relationship = st.selectbox("Relationship", enconders["relationship"].classes_)
native_country = st.selectbox("Native Country", enconders["native-country"].classes_)
sex = st.selectbox("Sex", enconders["sex"].classes_)
workclass = st.selectbox("Workclass", enconders["workclass"].classes_)
hours_per_week = st.slider("Hours per Week", 1, 99, 40)
capital_gain = st.number_input("Capital Gain", min_value=0, value=0)
nan = st.number_input("AGE", min_value=0, value=0)

# Encode categorical inputs based on notebook approach
encoded_inputs = {
    "education": enconders["education"].transform([education])[0],
    "marital-status": enconders["marital-status"].transform([marital_status])[0],
    "occupation": enconders["occupation"].transform([occupation])[0],
    "relationship": enconders["relationship"].transform([relationship])[0],
    "native-country": enconders["native-country"].transform([native_country])[0],
    "sex": enconders["sex"].transform([sex])[0],
    "workclass": enconders["workclass"].transform([workclass])[0],
}

# Create feature array using only notebook features
features = np.array([
    hours_per_week, capital_gain,nan,
    encoded_inputs["education"], encoded_inputs["marital-status"],
    encoded_inputs["occupation"], encoded_inputs["relationship"],
    encoded_inputs["native-country"], encoded_inputs["sex"],
    encoded_inputs["workclass"]
]).reshape(1, -1)

# Predict
if st.button("Predict Income"):
    prediction = dt_model.predict(features)[0]
    result = " YOUR INCOME IS LESS THAN 50K DOLLORS " if prediction == 1 else "YOUR INCOME IS GREATER THAN 50 k "
    st.success(f"Predicted Income: {result}")
