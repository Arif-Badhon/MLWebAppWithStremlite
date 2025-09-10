"""
@author: blackcat
@file: main.py
@time: 2024/6/20 16:45
@desc: Entry point for the ML web application.
"""
import streamlit as st
import joblib



def main():
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h1 style="color:white;text-align:center;">Welcome to the ML Web App</h1>
    </div>
    """

    st.markdown(html_temp, unsafe_allow_html=True)

    model = joblib.load("insurance_model")
    st.sidebar.title("Navigation")
    p1 = st.slider('Enter your age', 0, 18, 100)
    s1 = st.selectbox('Sex',('Male', 'Female', 'Other'))
    if s1=='Male':
        p2=1
    else:
        p2=0
    
    p3 = st.number_input('Enter your BMI', 0.0, 100.0, 25.0)
    p4 = st.number_input('Enter your number of children', 0, 20, 0)
    s2 = st.selectbox('Do you smoke?',('Yes', 'No'))
    if s2=='Yes':
        p5=1
    else:
        p5=0
    s3 = st.selectbox('Region',('Northeast', 'Northwest', 'Southeast', 'Southwest'))
    if s3=='Northeast':
        p6=0
        p7=0
        p8=0
    elif s3=='Northwest':
        p6=1
        p7=0
        p8=0
    elif s3=='Southeast':
        p6=0
        p7=1
        p8=0
    else:
        p6=0
        p7=0
        p8=1        
    if st.button("Predict"):
        prediction = model.predict([[p1, p2, p3, p4, p5, p6, p7, p8]])
        st.success(f'Your insurance cost is $ {prediction[0]:.2f}') 
    if st.button("About"):
        st.text("Built with Streamlit")
        st.text("Author: blackcat")
    



if __name__ == "__main__":
    main()
