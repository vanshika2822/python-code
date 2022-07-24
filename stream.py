import streamlit as st


def user(text):
    return f'<h3 style=\'text-align: center; padding-top: 20px; color: green;\'>Answer: {text:.2f}</h4>'


st.markdown("<h1 style='text-align: center; padding-top: 60px; padding-bottom: 0px;'>Division</h1>",
            unsafe_allow_html=True)
st.markdown("<p style='text-align: center; padding-top: 0px; padding-bottom: 40px;'>Divide Two Numbers using Streamlit</p>",
            unsafe_allow_html=True)


col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input('Enter First Number (numerator)', value=1.0)

with col2:
    num2 = st.number_input('Enter Second Number (Denominator)', value=1.0)


with st.empty():
    if num2 == 0:
        st.error('Cannot Divide by Zero!! Please, enter valid input')
    else:
        if st.button('Divide'):
            if num2 != 0:
                st.write(user(num1 / num2),
                         unsafe_allow_html=True)
                
