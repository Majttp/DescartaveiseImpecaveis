import streamlit as st
from database import criar_tabela

st.set_page_config(
    page_title="Descartáveis & Impecáveis",
    page_icon="📚",
    layout="centered"
)

criar_tabela()

st.title("📚 Descartáveis & Impecáveis")
st.caption("Livraria digital • Novos e usados com propósito")
