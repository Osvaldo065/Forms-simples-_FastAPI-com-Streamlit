import streamlit as st
import requests

#Parte inicial dos titulos e textos 
st.title("Formulário do usuário")
st.text("Preencha suas informções nutricionais")

#formulario para receber os dados
st.subheader("Digite seu Nome:")
nome = st.text_input("Nome:")

st.subheader("Digite seu sobrenome: ")
sobrenome = st.text_input("Sobrenome: ")

st.subheader("Digite sua idade:")
idade = st.text_input("Idade: ")

st.subheader("Digite seu peso: ")
pesoKg = st.text_input("peso Kg: ")

#Botão para salvar e armazenar os dados fazendo a comunicação com a API
if st.button("Salvar"):
    #Condicional para passar os atributos que receberão os dados e comunicarão com a API
    if nome and sobrenome and idade and pesoKg:
        dados = {
            "nome": nome,
            "sobrenome": sobrenome,
            "idade": idade,
            "pesoKg": float(pesoKg)
        }
        #var para receber resposta da conexão com a API
        resposta = requests.post("http://127.0.0.1:8000/usuarios", json=dados)
        
        #Condicional para verificar se a API funcionou 
        if resposta.status_code == 200: #Status 200 é para sinalizar que está OK
            st.success("Informações cadastradas com sucesso!!")
        else:
            st.error("Erro ao salvar os dados na API")
    else:
        st.warning("Preencha todos os campos!")
    
#Condicional para visualizar lista de usuarios 
if st.button("Ver usuários cadastrados"):
    #Variavel que recebe a requisição da API para chamar todos os usuarios.
    resposta = requests.get("http://127.0.0.1:8000/usuarios")
    
    
    if resposta.status_code == 200:
        #Variavel usuarios está recebendo as requisição da API pelo JSON
        usuarios = resposta.json()
        st.subheader("Lista de usuarios:")
        #Estrutura de repetição para exibir os dados que foram passados para a API. 
        for u in usuarios: 
            st.text(f"{u['nome']} {u['sobrenome']} - Idade: {u['idade']} -Peso: {u['pesoKg']} Kg")
        else:
            st.error("Erro ao buscar usuarios.")
    
    
    
    
    
    