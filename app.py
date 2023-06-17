import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('rf_healthcare.pkl', 'rb'))

def welcome():
    st.title(":green[Welcome to Homepage! 👋]")
    st.header(":blue[Car Price Prediction :car]")
    st.write('By: :red[Bharathkumar M S]')

    st.write(" :green[For Prediction select page to 'Prediction' in side bar]")
   
        


    btn_click = st.button("Click me to Know Who I am")

    if btn_click == True:
        st.subheader("You clicked me :cry:")
        st.balloons()
        st.title("I am :red[Bharathkumar M S]")
        st.title("I am a  :violet[ Data Science Enthusiast]")
        st.write("## Connect me on Linkedin [link](https://www.linkedin.com/in/bharathkumar-m-s-1736221b0/)")



def submit():
    st.title('Prediction')
    pregnancies = st.number_input('Pregnancies', value=0, min_value=0, step=1)
    glucose = st.number_input('Glucose', value=0, min_value=0, step=1)
    bloodpressure = st.number_input('Blood Pressure', value=0, min_value=0, step=1)
    skinthickness = st.number_input('Skin Thickness', value=0, min_value=0, step=1)
    insulin = st.number_input('Insulin', value=0, min_value=0, step=1)
    diabetes_pedigree_function = st.number_input('Diabetes Pedigree Function', value=0.0, min_value=0.0)
    bmi = st.number_input('BMI', value=0.0, min_value=0.0)
    age = st.number_input('Age', value=0, min_value=0, step=1)

    if st.button('Prediction'):
        result = model.predict([[pregnancies, glucose, bloodpressure, skinthickness, insulin, diabetes_pedigree_function, bmi, age]])

        if result == 0:
            st.text('Prediction: Non-Diabetic')
        else:
            st.text('Prediction: Diabetic')

# Set up the app layout
st.sidebar.title('Navigation')
page = st.sidebar.selectbox('Select Page', ['Welcome', 'Prediction'])

# Render the selected page
if page == 'Welcome':
    welcome()
elif page == 'Prediction':
    submit()
