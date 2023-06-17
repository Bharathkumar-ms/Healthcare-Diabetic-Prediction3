import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('rf_healthcare.pkl', 'rb'))

def welcome():
    st.title('Welcome')
    # Your code for the welcome page goes here
    # ...

def submit():
    st.title('Submit')
    pregnancies = st.number_input('Pregnancies', value=0, min_value=0, step=1)
    glucose = st.number_input('Glucose', value=0, min_value=0, step=1)
    bloodpressure = st.number_input('Blood Pressure', value=0, min_value=0, step=1)
    skinthickness = st.number_input('Skin Thickness', value=0, min_value=0, step=1)
    insulin = st.number_input('Insulin', value=0, min_value=0, step=1)
    diabetes_pedigree_function = st.number_input('Diabetes Pedigree Function', value=0.0, min_value=0.0)
    bmi = st.number_input('BMI', value=0.0, min_value=0.0)
    age = st.number_input('Age', value=0, min_value=0, step=1)

    if st.button('Submit'):
        result = model.predict([[pregnancies, glucose, bloodpressure, skinthickness, insulin, diabetes_pedigree_function, bmi, age]])

        if result == 0:
            st.text('Prediction: Non-Diabetic')
        else:
            st.text('Prediction: Diabetic')

# Set up the app layout
st.sidebar.title('Navigation')
page = st.sidebar.selectbox('Select Page', ['Welcome', 'Submit'])

# Render the selected page
if page == 'Welcome':
    welcome()
elif page == 'Submit':
    submit()
