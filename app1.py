import streamlit as st
import requests
import json

# Title of the app
st.title("Diabetes Prediction App")

import streamlit as st

# Title of the app
st.title("Diabetes Prediction Input Form")

# Instructions for each input field
st.write("Please enter the following details for diabetes prediction:")

# Input for pregnancies
pregnancies = st.number_input(
    "Pregnancies (0 - 20)", 
    min_value=0, 
    max_value=20, 
    help="Enter the number of pregnancies (maximum: 20)."
)

# Input for glucose
glucose = st.number_input(
    "Glucose (0 - 200)", 
    min_value=0, 
    max_value=200, 
    help="Enter the glucose level (maximum: 200 mg/dL)."
)

# Input for blood pressure
blood_pressure = st.number_input(
    "Blood Pressure (0 - 200)", 
    min_value=0, 
    max_value=200, 
    help="Enter the blood pressure level (maximum: 200 mm Hg)."
)

# Input for skin thickness
skin_thickness = st.number_input(
    "Skin Thickness (0 - 100)", 
    min_value=0, 
    max_value=100, 
    help="Enter the skin thickness (maximum: 100 mm)."
)

# Input for insulin
insulin = st.number_input(
    "Insulin (0 - 800)", 
    min_value=0, 
    max_value=800, 
    help="Enter the insulin level (maximum: 800 µU/mL)."
)

# Input for BMI
bmi = st.number_input(
    "BMI (0.0 - 70.0)", 
    min_value=0.0, 
    max_value=70.0, 
    help="Enter the Body Mass Index (BMI) (maximum: 70.0)."
)

# Input for diabetes pedigree function
diabetes_pedigree_function = st.number_input(
    "Diabetes Pedigree Function (0.0 - 2.5)", 
    min_value=0.0, 
    max_value=2.5, 
    help="Enter the diabetes pedigree function (maximum: 2.5)."
)

# Input for age
age = st.number_input(
    "Age (15 - 120)", 
    min_value=15, 
    max_value=120, 
    help="Enter the age (maximum: 120 years)."
)



# Button to send the input for prediction
if st.button("Submit"):
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
