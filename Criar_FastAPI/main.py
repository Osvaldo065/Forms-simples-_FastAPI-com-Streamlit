from fastapi import FastAPI
from pydantic import BaseModel
from decimal import Decimal

#Variavel para recener a função FastAPI
app = FastAPI()

#Classe com o atributos da API
class Usuario(BaseModel):
    nome: str
    sobrenome: str
    idade: str
    pesoKg: Decimal

#Variavel que gera uma lista para salvar os dados temporariamente
usuarios = []
    
#Rota inicial para verificar se a API está funcionando
@app.get("/")

def home():
    return {"Mensagem": "API está rodando!"}

#Rota para Adicionar/Atualizar o Usuario - POST
@app.post("/usuarios")
def criar_usuarios(usuario: Usuario):
    usuarios.append(usuario)
    return{"Mensagem": "Usuário criado com sucesso!"}

#Rota para chamar os usuarios - GET
@app.get("/usuarios")

#Função para listar os usuarios
def listar_usuarios():
    return usuarios
