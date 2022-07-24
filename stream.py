##import streamlit as st
##import pandas as pd
##
##st.write("""
###Division of two numbers
##""")
##
##st.header('User input parameters')
##
##def user():
##    num1=st.number_input("Enter first number",min_value=0.0,max_value=2000000.00)
##    num2=st.number_input("Enter second number",min_value=0.0,max_value=2000000.00)
##    num3=st.number_input("Result",num1/num2)
####    data={'number 1':num1,
####          'number2':num2}
####    
####    feature=pd.DataFrame(data)
####    return feature
####
####df=user()
####st.write(df)
##user()

import streamlit as st


def answer(text):
    return f'<h4 style=\'text-align: center; padding-top: 20px; color: green;\'>Answer: {text:.2f}</h4>'


st.markdown("<h1 style='text-align: center; padding-top: 60px; padding-bottom: 0px;'>Division</h1>",
            unsafe_allow_html=True)
st.markdown("<p style='text-align: center; padding-top: 0px; padding-bottom: 40px;'>Divide Two Numbers using Streamlit</p>",
            unsafe_allow_html=True)


col1, col2 = st.columns(2)

with col1:
    num_one = st.number_input('First Number (numerator)', value=1.0)

with col2:
    num_two = st.number_input('Second Number (Denominator)', value=1.0)


with st.empty():
    if num_two == 0:
        st.error('Cannot Divide by Zero')
    else:
        if st.button('Divide'):
            if num_two != 0:
                st.write(answer(num_one / num_two),
                         unsafe_allow_html=True)

    
