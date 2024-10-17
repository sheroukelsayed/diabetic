import streamlit as st
import requests
import json

# Title of the app
st.title("Diabetes Prediction App")

# Collect input from the user
st.write("Enter the details for the prediction:")
pregnancies = st.number_input("Pregnancies", min_value=0)
glucose = st.number_input("Glucose", min_value=0)
blood_pressure = st.number_input("Blood Pressure", min_value=0)
skin_thickness = st.number_input("Skin Thickness", min_value=0)
insulin = st.number_input("Insulin", min_value=0)
bmi = st.number_input("BMI", min_value=0.0)
diabetes_pedigree_function = st.number_input("Diabetes Pedigree Function", min_value=0.0)
age = st.number_input("Age", min_value=15)

# Button to send the input for prediction
if st.button("Predict"):
    # Prepare the input data
    input_data = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]
    input_data_json = json.dumps({"data": [input_data]})

    # Replace with your deployed Azure endpoint
    scoring_uri = "http://6dc02ede-2595-4f65-a718-11675b73b5fd.westus2.azurecontainer.io/score"

    # Define the headers
    headers = {"Content-Type": "application/json"}

    # Send the POST request to the API
    response = requests.post(scoring_uri, data=input_data_json, headers=headers)

    # Process the response
    if response.status_code == 200:
        result = json.loads(response.json())
        #print(result)
        prediction = result["result"][0]
        st.success(f"The predicted diabetes risk is: {'High' if prediction == 1 else 'Low'}")
    else:
        st.error(f"Error: {response.text}")
