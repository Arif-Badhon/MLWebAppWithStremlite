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


if __name__ == "__main__":
    main()
