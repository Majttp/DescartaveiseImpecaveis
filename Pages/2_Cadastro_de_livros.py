import streamlit as st
from database import inserir_livro

st.title("📝 Cadastro de Livros")

with st.form("form_livro"):
    titulo = st.text_input("Título do livro")
    autor = st.text_input("Autor")
    categoria = st.selectbox("Categoria", ["Romance", "Educação", "Ficção", "Infantil", "Outro"])
    tipo = st.radio("Tipo", ["Impecável", "Descartável"])
    preco = st.number_input("Preço (R$)", min_value=0.0, format="%.2f")
    descricao = st.text_area("Descrição")

    enviado = st.form_submit_button("Cadastrar livro")

if enviado:
    with st.spinner("Salvando livro..."):
        inserir_livro(titulo, autor, categoria, tipo, preco, descricao)
    st.success("📚 Livro cadastrado com sucesso!")
