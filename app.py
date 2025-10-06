#app.py
import streamlit as st
from crud import criar_aluno, listar_alunos, atualizar_alunos, deletar_aluno
# precisa instalar o streamlit
# pip install streamlit
# config nome da pagina
st.set_page_config(page_title="Gerenciamento de alunos", page_icon=":books:")

st.title("Sistema de alunos com PostgreSQL") 

menu = st.sidebar.radio("menu", ["Criar", "Listar", "Atualizar", "Deletar"])

if menu == "Criar":
    st.subheader("➕Criar aluno")
    nome = st.text_input("Nome do aluno") 
    idade = st.number_input("idade", min_value=14, step=1)
    if st.button("Cadastrar"):
        if nome.strip() != "":
            criar_aluno(nome, idade)
            st.success(f"Aluno {nome} foi cadastrado com sucesso!")
        else:
            st.warning("O campo nome não pode estar vazio")
elif menu == "listar":
    st.subheader("Listar alunos")
    alunos = listar_alunos()
    if alunos:
        st.table(alunos)
    else:
        st.info("nenhum aluno encontrado")


elif menu == "Atualizar":
    st.subheader("Atualizar idade")
    alunos = listar_alunos()
    if alunos:
        id_aluno = st.selectbox("Escolha o aluno",[linha[0] for linha in alunos])
        nova_idade = st.number_input("Nova idade", min_value=10, step=1)
        st.button("Atualizar")
        atualizar_alunos(id_aluno,nova_idade )
        st.success(f"idade do aluno {id_aluno} atualizada com sucesso!")
    else:
        st.info("Nehum aluno disponível para atualidar")