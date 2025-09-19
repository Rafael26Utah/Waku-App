import streamlit as st

# --- Estilo da página ---
st.set_page_config(page_title="Waku App", page_icon="🔥", layout="centered")

# --- CSS para personalizar ---
st.markdown("""
    <style>
        .title {
            font-size: 40px;
            font-weight: bold;
            color: #4CAF50;
            text-align: center;
        }
        .subtitle {
            font-size: 20px;
            color: #555;
            text-align: center;
        }
        .welcome {
            font-size: 22px;
            color: #1E90FF;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# --- Cabeçalho ---
st.markdown('<p class="title">🔥 Aplicativo Waku - Teste 🔥</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Experimente a versão inicial do Waku App</p>', unsafe_allow_html=True)

# --- Entrada do usuário ---
nome = st.text_input("Digite o seu nome:")

if st.button("Enviar"):
    if nome.strip() != "":
        st.markdown(f"<p class='welcome'>👋 Olá, {nome}! Bem-vindo ao Waku 🚀</p>", unsafe_allow_html=True)
    else:
        st.warning("⚠ Por favor, digite um nome antes de enviar.")
