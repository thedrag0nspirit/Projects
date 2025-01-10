import streamlit as st
import pickle
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.feature_extraction.text import CountVectorizer
from scipy.sparse import hstack

data = st.info("Loading Models.......")

DT_model = pickle.load(open('models/DT.pkl', 'rb'))

V1 = pickle.load(open('models/Crop.pkl', 'rb'))

V2  = pickle.load(open('models/CostCultivation.pkl', 'rb'))

V3  = pickle.load(open('models/CostCultivation.pkl', 'rb'))

V4  = pickle.load(open('models/Production.pkl', 'rb'))

V5  = pickle.load(open('models/Yield.pkl', 'rb'))

V6  = pickle.load(open('models/Temperature.pkl', 'rb'))

V7  = pickle.load(open('models/RainFall_Annual.pkl', 'rb'))

data.success("Models Loaded")

st.title("Crop Price Prediction using ML ")
st.header('An ML project to predict the price of a crop using different parameters')
st.subheader("Project by Deepanshu Thakur")

st.image("1.jpg")

st.write("We are trying to predict the price of a crop using many different parameters. "
         "We are solving a real-life problem from indian gov data. It is a Regression problem where one has to predict a price of a crop "
         "with the features mentioned below")

st.subheader('Enter the details:')

with st.form("my_form"):

    state = st.selectbox('State :', ( 'UttarPradesh','Karnataka','Gujarat','Andhra Pradesh','Maharashtra',
                                      'Punjab','Haryana','Rajasthan','Madhya Pradesh','Tamil Nadu','Bihar',
                                      'Orissa','West Bengal'))

    crop = st.selectbox('Crop :', ('ARHAR','COTTON','GRAM','GROUNDNUT','MAIZE','MOONG','PADDY',' MUSTARD',
    'SUGARCANE','WHEAT'))

    crop_name = crop

    CostCultivation = st.number_input('CostCultivation :')

    CostCultivation2 = st.number_input('CostCultivation2 :')

    Production = st.number_input('Production :')

    Yield = st.number_input('Yield :')

    Temperature = st.number_input('Temperature :')

    RainFall_Annual = st.number_input('RainFall Annual:')

    submitted = st.form_submit_button("Predict price")

    crop = np.array(crop).reshape(1, -1)
    CostCultivation = np.array(CostCultivation).reshape(1, -1)
    CostCultivation2 = np.array(CostCultivation2).reshape(1, -1)
    Production = np.array(Production).reshape(1, -1)
    Yield = np.array(Yield).reshape(1, -1)
    Temperature = np.array(Temperature).reshape(1, -1)
    RainFall_Annual = np.array(RainFall_Annual).reshape(1, -1)


    crop =  V1.transform(crop.ravel())
    CostCultivation  = V2.transform(CostCultivation)
    CostCultivation2  = V3.transform(CostCultivation2)
    Production = V4.transform(Production)
    Yield = V5.transform(Yield)
    Temperature = V6.transform(Temperature)
    RainFall_Annual = V7.transform(RainFall_Annual)

    input= hstack((crop,CostCultivation,CostCultivation2,Production,Yield,Temperature,RainFall_Annual)).tocsr()

    predict = DT_model.predict(input)
    output = str(int(predict[0]))

    o1 = "Predicted price of your crop (" + crop_name + ") : " + output + "₹"

    if submitted:
        st.success(o1)
