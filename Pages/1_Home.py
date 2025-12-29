import streamlit as st

st.title("🏠 Bem-vindo à Livraria")

st.image("Imagens/loading.gif", use_column_width=True)

st.markdown("""
### 📖 Nossa proposta
A **Descartáveis & Impecáveis** é uma livraria que valoriza livros novos e usados,
promovendo acesso à leitura e consumo consciente.

Aqui você encontra:
- Livros impecáveis (novos ou como novos)
- Livros descartáveis (usados, raros ou doações)
""")

st.info("✨ Projeto desenvolvido em Streamlit como trabalho final de curso.")
