import numpy as np
import pandas as pd
import pickle as pkl
import streamlit as st

# Streamlit styles for background color
st.markdown(
    """
    <style>
        body {
            background-color: #98FF98;
        }
        .block-container {
            background-color: #98FF98;
        }
        .sidebar .sidebar-content {
            background-color: #98FF98;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Load the pre-trained model
model = pkl.load(open('linear_regression_model.pkl', 'rb'))

# Set the header
st.header('CAR PRICE PREDICTION MODEL ALONG WITH TAX CALCULATIONS')

# Load car data
car_data = pd.read_csv('C:/Users/ASUS/Documents/car_prediction_data.csv')
car_data['Car_Name'] = car_data['Car_Name'].apply(lambda x: x.split(' ')[0])

# User input fields
car_name = st.selectbox('Select Car Brand', car_data['Car_Name'].unique())
year = st.selectbox('Manufactured Year', list(range(2007, 2015)))
kms_driven = st.slider('No. of kms Driven', 500, 500000)
fuel_type = st.selectbox('Select Fuel type', car_data['Fuel_Type'].unique())
seller_type = st.selectbox('Select Seller type', car_data['Seller_Type'].unique())
transmission = st.selectbox('Select Transmission', car_data['Transmission'].unique())
owner = st.selectbox('Select Owner', car_data['Owner'].unique())
present_price = st.slider('Present price of Car', 30000, 3500000)

# Prediction logic on button click
if st.button("Predict"):
    # Prepare input data
    x_test = pd.DataFrame(
        [[present_price, kms_driven, owner, year, car_name, fuel_type, seller_type, transmission]],
        columns=['Present_Price', 'Kms_Driven', 'Owner', 'Year', 'Car_Name_encoded', 'Fuel_Type_encoded', 'Seller_Type_encoded', 'Transmission_encoded']
    )

    # Encoding categorical variables
    x_test['Fuel_Type_encoded'].replace(['Petrol', 'Diesel', 'CNG'], [2, 1, 0], inplace=True)
    x_test['Seller_Type_encoded'].replace(['Dealer', 'Individual'], [0, 1], inplace=True)
    x_test['Transmission_encoded'].replace(['Manual', 'Automatic'], [1, 0], inplace=True)
    x_test['Car_Name_encoded'].replace(
        ['ritz', 'sx4', 'ciaz', 'wagon', 'swift', 'vitara', 's', 'alto',
         'ertiga', 'dzire', 'ignis', '800', 'baleno', 'omni', 'fortuner',
         'innova', 'corolla', 'etios', 'camry', 'land', 'Royal', 'UM',
         'KTM', 'Bajaj', 'Hyosung', 'Mahindra', 'Honda', 'Yamaha', 'TVS',
         'Hero', 'Activa', 'Suzuki', 'i20', 'grand', 'i10', 'eon', 'xcent',
         'elantra', 'creta', 'verna', 'city', 'brio', 'amaze', 'jazz'],
        [36, 39, 18, 42, 38, 41, 37, 13, 25, 22, 31, 0, 15, 35, 27, 32, 20,
         26, 17, 34, 8, 11, 6, 2, 5, 7, 4, 12, 10, 3, 1, 9, 30, 28,
         29, 24, 43, 23, 21, 40, 19, 16, 14, 33],
        inplace=True
    )

    # Scale down present price
    x_test['Present_Price'] = x_test['Present_Price'] * (10 ** -5)

    # Predict the selling price
    selling_price_predicted = model.predict(x_test)
    predicted_price = selling_price_predicted[0][0] * (10 ** 5)

    # Check for negative prediction and display appropriate message
    if predicted_price < 0:
        st.markdown(
            '<p style="font-size: 20px; color: red;">Invalid data: The model predicted a negative selling price. Please verify the inputs.</p>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<p style="font-size: 20px; color: red;">Calculated tax is also invalid due to negative prediction.</p>',
            unsafe_allow_html=True
        )
    else:
        # Calculate tax price
        tax_price = 0.18 * (present_price - predicted_price)

        # Display the predicted selling price
        st.markdown(
            '<p style="font-size: 20px;">Predicted Selling Car Price is around:</p> <p style="color: skyblue; font-size: 20px;"> ₹ ' +
            str(round(predicted_price, 2)) + "</p>", unsafe_allow_html=True
        )

        # Display the calculated tax price
        st.markdown(
            '<p style="font-size: 20px;">Calculated Tax Price:</p> <p style="color: orange; font-size: 20px;"> ₹ ' +
            str(round(tax_price, 2)) + "</p>", unsafe_allow_html=True
        )
