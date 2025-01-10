Crop Price Prediction Using Machine Learning
Crop Price Prediction App 🌾
This repository contains a Streamlit-based web application for predicting crop prices using machine learning. The application leverages a trained DecisionTreeRegressor model and various preprocessed features to estimate the price of a crop based on user-provided inputs like production, yield, temperature, and rainfall.

Features 🚀
Interactive Web Interface: Built with Streamlit for seamless user interaction.
Machine Learning Model: Uses a pre-trained DecisionTreeRegressor for price prediction.
Data Transformation: Incorporates vectorizers for processing categorical and numerical inputs.
Customizable Inputs: Allows users to specify state, crop type, and other agricultural parameters.
Real-Time Predictions: Instantly predicts crop prices based on the provided inputs.


Installation 🛠️
Prerequisites
Python 3.7 or higher
Streamlit
Required Python libraries: pickle, numpy, scipy, scikit-learn
Setup
Clone the repository:
git clone https://github.com/<your_username>/crop-price-prediction.git
cd crop-price-prediction
pip install -r requirements.txt
Place the pre-trained model and vectorizer files (DT.pkl, Crop.pkl, etc.) in the models/ directory.

Add an image named 1.jpg (used in the UI) in the root folder or replace with your own image.

Run the app:streamlit run app.py
Usage 🧑‍🌾
Open the app in your browser (default: http://localhost:8501).
Select the state and crop type.
Enter the required agricultural parameters:
Cost of Cultivation
Additional Cultivation Costs
Production
Yield
Temperature
Annual Rainfall
Click Predict Price to get the estimated crop price.
File Structure 📁
crop-price-prediction/
│
├── models/                 # Directory for model and vectorizer files
│   ├── DT.pkl              # Trained DecisionTreeRegressor model
│   ├── Crop.pkl            # Vectorizer for crop type
│   ├── CostCultivation.pkl # Vectorizer for cost of cultivation
│   └── ...                 # Other vectorizers
│
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── 1.jpg                   # Placeholder image for the UI
└── README.md               # Project documentation
Contributing 🤝
Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

Future Enhancements 🌟
Add more crops and states to the prediction model.
Improve the accuracy of the model with additional features and retraining.
Integrate a database for real-time data storage.
Deploy the application on a cloud platform like Heroku or AWS.

License 📝
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments 🙏
Special thanks to the Indian government for providing open agricultural data and the Scikit-learn community for the tools used in this project.
