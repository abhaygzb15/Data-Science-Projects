import streamlit as st
import math
import pickle
import sklearn
from PIL import Image
with open('model.pkl','rb') as F:
    model=pickle.load(F)
st.markdown("<h1 style='text-align: center;'>Titanic Survival Prediction</h1>", unsafe_allow_html=True)
image =st.image('ship2.jpg')
st.markdown("<p style='text-align: right;'>Royal Mail Ship TITANIC</p>", unsafe_allow_html=True)
col1,col2,col3=st.columns(3)
with col1:
    Pclass=st.selectbox("Class of Passenger",("Premier","Executive","Economy"))
with col2:
    Sex=st.selectbox("Gender",("Male","Female"))
with col3:
    Age=st.number_input("Age of passenger")

col4,col5=st.columns(2)
with col4:
    SibSp=st.number_input("Siblings/Spouses")
with col5:
    Parch=st.number_input('Parents/Children')

Embarked = st.selectbox("Picking Point",("Cherbourg","Queenstown","Southampton"))

if st.button("Predict"):
    pclass=1
    if Pclass=="Economy":
        pclass=3
    if Pclass=="Executive":
        pclass=2

    gender=0
    if Sex=="Female":
        gender=0

    age = math.ceil(Age)
    sibSp = math.ceil(SibSp)
    parch = math.ceil(Parch)

    embarked = 0
    if Embarked == "Cherbourg":
        embarked = 1
    elif Embarked == "Queenstown":
        embarked = 2

    result = model.predict([[pclass, gender, age, sibSp, parch, embarked]])
    output_labels = {1: "The passenger will Survive.",
                     0: "The passenger will not survive."}
    st.markdown(f"## {output_labels[result[0]]}")





