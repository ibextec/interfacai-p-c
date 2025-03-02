import streamlit as st
import pandas as pd
import json

# Inicialização dos dados (se não existirem)
try:
    with open('data.json', 'r') as f:
        data = json.load(f)
except FileNotFoundError:
    data = {'chapas': [], 'fabricantes': [], 'clientes': [], 'pecas': [], 'fitas': [], 'acessorios': []}

def salvar_dados():
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4) # indent=4 para melhor visualização do arquivo JSON.

def cadastrar_chapa():
    st.subheader("Cadastro de Chapa")
    nome = st.text_input("Nome da Chapa")
    fabricante = st.selectbox("Fabricante", [f["nome"] for f in data["fabricantes"]])
    espessura = st.selectbox("Espessura (mm)", [3, 6, 9, 12, 15, 18, 25])
    dimensoes = st.text_input("Dimensões (LxC)")
    
    if st.button("Salvar Chapa"):
        nova_chapa = {
            "nome": nome,
            "fabricante": fabricante,
            "espessura": espessura,
            "dimensoes": dimensoes
        }
        data["chapas"].append(nova_chapa)
        salvar_dados()
        st.success("Chapa cadastrada com sucesso!")

def cadastrar_fabricante():
    st.subheader("Cadastro de Fabricante")
    nome = st.text_input("Nome do Fabricante")
    
    if st.button("Salvar Fabricante"):
        novo_fabricante = {"nome": nome}
        data["fabricantes"].append(novo_fabricante)
        salvar_dados()
        st.success("Fabricante cadastrado com sucesso!")
        
def cadastrar_cliente():
    st.subheader("Cadastro de Cliente")
    nome = st.text_input("Nome do Cliente")
    endereco = st.text_area("Endereço")
    telefone = st.text_input("Telefone")
        
    if st.button("Salvar Cliente"):
        novo_cliente = {"nome": nome, "endereco": endereco, "telefone": telefone}
        data["clientes"].append(novo_cliente)
        salvar_dados()
        st.success("Cliente cadastrado com sucesso!")

def cadastrar_peca():
    st.subheader("Cadastro de Peça")
    nome = st.text_input("Nome da Peça")
    dimensoes = st.text_input("Dimensões (LxC)")
    material = st.selectbox("Material",[c["nome"] for c in data["chapas"]])

    if st.button("Salvar Peça"):
        nova_peca = {"nome": nome, "dimensoes": dimensoes, "material" : material}
        data["pecas"].append(nova_peca)
        salvar_dados()
        st.success("Peça cadastrada com sucesso!")

def cadastrar_fita():
    st.subheader("Cadastro de Fita")
    nome = st.text_input("Nome da Fita")
    espessura = st.number_input("Espessura (mm)")
    cor = st.text_input("Cor")

    if st.button("Salvar Fita"):
        nova_fita = {"nome": nome, "espessura": espessura, "cor": cor}
        data["fitas"].append(nova_fita)
        salvar_dados()
        st.success("Fita cadastrada com sucesso!")

def cadastrar_acessorio():
    st.subheader("Cadastro de Acessório")
    nome = st.text_input("Nome do Acessório")
    descricao = st.text_area("Descrição")
    preco = st.number_input("Preço")

    if st.button("Salvar Acessório"):
        novo_acessorio = {"nome": nome, "descricao": descricao, "preco": preco}
        data["acessorios"].append(novo_acessorio)
        salvar_dados()
        st.success("Acessório cadastrado com sucesso!")

def main():
    st.title("Otimizador de Corte de Chapas")
    menu = st.sidebar.selectbox("Menu", ["Cadastro de Chapas", "Cadastro de Fabricantes", "Cadastro de Clientes", "Cadastro de Peças", "Cadastro de Fitas","Cadastro de Acessórios"])

    if menu == "Cadastro de Chapas":
        cadastrar_chapa()
    elif menu == "Cadastro de Fabricantes":
        cadastrar_fabricante()
    elif menu == "Cadastro de Clientes":
        cadastrar_cliente()
    elif menu == "Cadastro de Peças":
        cadastrar_peca()
    elif menu == "Cadastro de Fitas":
        cadastrar_fita()
    elif menu == "Cadastro de Acessórios":
        cadastrar_acessorio()
    # Adicione as funcionalidades de cálculo, layout e exportação aqui.

if __name__ == "__main__":
    main()
