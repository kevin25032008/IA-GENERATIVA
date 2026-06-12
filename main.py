#Investimento de marketing


import numpy as np 
from sklearn.linear_model import LinearRegression
#investimento em mkt 1mil
X = np.array([[1],[2],[4],[5],[3]])
# vendas
y = np.array ([2,8,4,6,5])

modelo = LinearRegression()
modelo.fit(X,y)

print(modelo.predict([[6]]))

#import numpy as np 
#from sklearn.linear_model import LinearRegression
#investimento em mkt 1mil
#X = np.array([[1],[2],[4],[5],[3]])
# vendas
#y = np.array ([2,8,4,6,5])

#modelo = LinearRegression()
#modelo.fit(X,y)

#print(modelo.predict([[6]]))

import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.header('Previsão de Vendas')

# Dados: [Investimento em Marketing] -> Faturamento
dados_vendas = pd.DataFrame({
    'investimento': [100, 200, 300, 400, 500, 600],
    'faturamento': [1200, 2500, 3200, 4800, 5100, 6300]
})

# Separando variáveis
X = dados_vendas [['investimento']]
y = dados_vendas ['faturamento']

# Treinando modelo
modelo=LinearRegression
modelo.fit(X,y)

# Entrada do usuário
investimento_futuro = number_input(
    'informe o investimento em marketing',
    min_value=0.0,
    value=700.0
)

#Previsão
if st.button('prever Faturamento'):
    previsão = modelo.predict([[investimento_futuro]])[0]

    st.success(
        f'Faturamento previsto para R$ {investimento_futuro:,.2f}'
        f'wm investimento: R$ {previsão:,.2f}'
    )

#Exibir dados utilizados
st.subheader('Dados de Treinamento')
st.dataframe(dados_vendas)


