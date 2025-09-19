import streamlit as st

# Título do aplicativo
st.title("Aplicativo Waku - Teste")

# Entrada de texto
nome = st.text_input("Digite o seu nome:")

# Botão
if st.button("Enviar"):
    st.write(f"Olá, {nome}! 👋 Bem-vindo ao Waku.") 
