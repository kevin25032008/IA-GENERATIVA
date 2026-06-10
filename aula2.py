import streamlit as st
import pandas as pd

#depurar

st.title('isso é um titulo')
st.button('clique aqui')
st.write('isso é um paragrafo')
st.map()

dados = {
'vendas':[100,20,30,60],
'mês':['jan','fev','mar','abril']
}

if st.button('clique aqui' , key='botao_a'):
    st.write('A')
    d= pd.read_csv('dados.csv')
    df = pd.DataFrame(dados)
    st.line_chart(df ,x='mês' , y='vendas')

    st.bar_chart(df, x='mês', y='vendas')
    st.scatter_chart(df, x='mês', y='vendas')

    st.title('❤️')
    