import streamlit as st
from database import listar_livros, atualizar_livro

st.title("📚 Catálogo de Livros")

df = listar_livros()

if df.empty:
    st.warning("Nenhum livro cadastrado ainda.")
else:
    st.dataframe(df)

    st.markdown("---")
    st.subheader("✏️ Editar livro")

    livro_id = st.selectbox("Selecione o ID do livro", df["id"])

    livro = df[df["id"] == livro_id].iloc[0]

    titulo = st.text_input("Título", livro["titulo"])
    autor = st.text_input("Autor", livro["autor"])
    categoria = st.text_input("Categoria", livro["categoria"])
    tipo = st.selectbox("Tipo", ["Impecável", "Descartável"], index=0 if livro["tipo"]=="Impecável" else 1)
    preco = st.number_input("Preço", value=float(livro["preco"]))
    descricao = st.text_area("Descrição", livro["descricao"])

    if st.button("Atualizar livro"):
        atualizar_livro(livro_id, titulo, autor, categoria, tipo, preco, descricao)
        st.success("✅ Livro atualizado com sucesso!")
