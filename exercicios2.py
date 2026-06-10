#calculadora

import streamlit as st

st.title('calculadora')

numero1 = st.number_input('numero')
numero2 = st.number_input('numero', step=0.1)

if st.button('RESULTADO'):
    soma = numero1 + numero2
    st.success(soma)

#calculadora de imc
st.title('calculo do imc')

peso = st.number_input('PESO')
altura = st.number_input('ALTURA')

if st.button ('calculadora imc'):
    calculo = round(peso/ (altura**2))
    st.success(calculo)

if st.button('-'):
        soma = numero1-numero2
        st.success(soma)

if st.button('+'):
        soma = numero1+numero2
        st.success(soma)

if st.button('/'):
        soma = numero1/numero2
        st.success(soma)

if st.button('*'):
        soma = numero1*numero2
        st.success(soma)       