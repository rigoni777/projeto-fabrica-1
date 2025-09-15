import streamlit as st
import guarda_funcoes as gf

st.title("Medias das notas da escola!")
st.caption("Calcule suas notas!😉")

with st.sidebar:
    botao_calcular = st.button("Calculadora das suas notas")

nome = st.text_input("Nome do Aluno: ")
nota1 = st.slider(min_value=0.0, max_value=10.0,label="Nota 1",step=0.25)
nota2 = st.slider(min_value=0.0, max_value=10.0,label="Nota 2",step=0.25)
nota3 = st.slider(min_value=0.0, max_value=10.0,label="Nota 3",step=0.25)
nota4 = st.slider(min_value=0.0, max_value=10.0,label="Nota 4",step=0.25)
nota5 = st.slider(min_value=0.0, max_value=10.0,label="Nota 5",step=0.25)

botao = st.button("Enviar")

if botao:
    media = gf.calcula_media(nota1,nota2,nota3,nota4)
    situacao= gf.situacao_media(media)
    texto = f"O aluno: {nome}, esta {situacao}, com media: {media}"
    if situacao == "Aprovado":
        st.success(texto)
    elif situacao == "Recuperação":
        st.warning(texto)
    else:
        st.error(texto)
