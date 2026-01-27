import streamlit as st
import pandas as pd
import joblib

# Load trained pipeline
model = joblib.load("housing_price_model.pkl")

st.title("🏠 California Housing Price Prediction")
st.write("Enter housing details to predict median house value")

# User inputs (match dataset columns EXACTLY)
longitude = st.number_input("Longitude", value=-122.23)
latitude = st.number_input("Latitude", value=37.88)
housing_median_age = st.number_input("Housing Median Age", value=41)
total_rooms = st.number_input("Total Rooms", value=880)
total_bedrooms = st.number_input("Total Bedrooms", value=129)
population = st.number_input("Population", value=322)
households = st.number_input("Households", value=126)
median_income = st.number_input("Median Income", value=8.3)
ocean_proximity = st.selectbox(
    "Ocean Proximity",
    ["<1H OCEAN", "INLAND", "ISLAND", "NEAR BAY", "NEAR OCEAN"]
)

# Create dataframe (VERY IMPORTANT: column names must match training data)
input_df = pd.DataFrame({
    "longitude": [longitude],
    "latitude": [latitude],
    "housing_median_age": [housing_median_age],
    "total_rooms": [total_rooms],
    "total_bedrooms": [total_bedrooms],
    "population": [population],
    "households": [households],
    "median_income": [median_income],
    "ocean_proximity": [ocean_proximity]
})

if st.button("Predict Price"):
    prediction = model.predict(input_df)
    st.success(f"🏷️ Predicted Median House Value: ${prediction[0]:,.2f}")
