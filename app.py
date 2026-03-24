import streamlit as st
import joblib
import pandas as pd

model = joblib.load("model/model.pkl")

st.title("Car Price Predictor")

present_price = st.number_input("Present Price")
kms_driven = st.number_input("Kms Driven")
owner = st.number_input("Owner (0,1,2)")
car_age = st.number_input("Car Age")

fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel"])
seller = st.selectbox("Seller Type", ["Dealer", "Individual"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])

# convert to correct format
fuel_diesel = 1 if fuel == "Diesel" else 0
fuel_petrol = 1 if fuel == "Petrol" else 0
seller_individual = 1 if seller == "Individual" else 0
transmission_manual = 1 if transmission == "Manual" else 0

if st.button("Predict"):
    input_data = pd.DataFrame([[present_price, kms_driven, owner, car_age,
                                fuel_diesel, fuel_petrol,
                                seller_individual, transmission_manual]],
                              columns=['Present_Price', 'Kms_Driven', 'Owner', 'Car_Age',
                                       'Fuel_Type_Diesel', 'Fuel_Type_Petrol',
                                       'Seller_Type_Individual', 'Transmission_Manual'])

    prediction = model.predict(input_data)
    st.success(f"Predicted Price: {prediction[0]:.2f}")