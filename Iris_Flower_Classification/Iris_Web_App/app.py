import streamlit as st
import math
import pickle
import sklearn
with open('model.pkl','rb') as F:
    model=pickle.load(F)

st.markdown("<h1 style='text-align: center;'>Iris  Flower  Classification</h1>", unsafe_allow_html=True)
image =st.image('iris_species.png')
S_L=st.number_input("Sepal Length")
S_W=st.number_input("Sepal Width")
P_L=st.number_input("Petal Length")
P_W=st.number_input("Petal Width")
if st.button("Predict"):
    result = model.predict([[S_L,S_W,P_L,P_W]])
    output_labels = {0: "This is Iris-setosa.",
                     1: "TThis is Iris-versicolor.",
                     2: "This is Iris-Virginica."}
    st.markdown(f"## {output_labels[result[0]]}")
    if (result[0]==0):
        image = st.image('setosa.jpeg')
    elif (result[0]==1):
        image = st.image('versicolor.jpeg')
    else:
        image = st.image('virginica.jpeg')




