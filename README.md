# ML-PROJECT-CAR-PRICE-PREDICTION-MODEL:
[car-price-prediction-model](https://ml-project-car-price-prediction-model-tgokbxqcfprv9hb5dk3tke.streamlit.app/)

Car Price Prediction Model: A Streamlit-based machine learning application for predicting car prices after taxes. Users can input car details like brand, manufacturing year, kilometers driven, fuel type, and more to get an estimated selling price along with tax calculations.
# Features:-
1)Predicts car prices after taxes based on various factors.
2)Interactive and intuitive UI with dropdowns, sliders, and buttons.
3)Displays both the estimated price and tax calculations.
4)Handles invalid predictions and notifies users appropriately.

# Technologies Used:-
Python
Streamlit (for the web app)
NumPy (for numerical operations)
Pandas (for data manipulation)
Scikit-learn (for the machine learning model)

# Setup Instructions:-
1)Clone the repository: git clone https://github.com/your-username/ML-PROJECT-CAR-PRICE-PREDICTION-MODEL.git
2)Navigate to the project folder: cd your-repository-name
3)Install dependencies: pip install -r requirements.txt
4)Run the app: streamlit run app.py

# How to Use:-
1)Select the car's brand, fuel type, seller type, transmission type, and owner type using the dropdown menus.

2)Use the sliders to set the car's present price and kilometers driven.

3)Click Predict to get the estimated selling price and tax.

# File Structure:-
1)app.py: Main Streamlit app code.

2)linear_regression_model.pkl: Pre-trained machine learning model for prediction.

3)car_prediction_data.csv: Dataset used for encoding and dropdowns.

4)requirements.txt: List of dependencies.

# Deployment:-
This app is deployed on Streamlit Community Cloud for easy access. To deploy, push your code to a GitHub repository and configure the app on Streamlit Community Cloud.

# License:-
This project is licensed under the MIT License. You are free to use, modify, and distribute it as needed.
