import streamlit as st
import pandas as pd
import json
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Inicialização dos dados com cadastros de demonstração
data = {
    'chapas': [
        {'nome': 'MDF Branco TX', 'fabricante': 'Duratex', 'espessura': 18, 'dimensoes': '2750x1840'},
        {'nome': 'MDP Carvalho', 'fabricante': 'Arauco', 'espessura': 15, 'dimensoes': '2750x1830'},
        {'nome': 'MDF Preto', 'fabricante': 'Eucatex', 'espessura': 6, 'dimensoes': '2750x1840'},
    ],
    'fabricantes': [
        {'nome': 'Duratex'},
        {'nome': 'Arauco'},
        {'nome': 'Eucatex'},
        {'nome': 'Guararapes'},
    ],
    'clientes': [
        {'nome': 'João Silva', 'endereco': 'Rua A, 123', 'telefone': '11 99999-9999'},
        {'nome': 'Maria Oliveira', 'endereco': 'Av. B, 456', 'telefone': '21 88888-8888'},
    ],
    'pecas': [
        {'nome': 'Prateleira 1', 'dimensoes': '800x300', 'material': 'MDF Branco TX', 'quantidade': 2},
        {'nome': 'Lateral Gaveta', 'dimensoes': '500x150', 'material': 'MDP Carvalho', 'quantidade': 4},
    ],
    'fitas': [],
    'acessorios': []
}

def salvar_dados():
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)

def cadastrar_fabricante():
    st.subheader("Cadastro de Fabricante")
    nome = st.text_input("Nome do Fabricante")
    
    if st.button("Salvar Fabricante"):
        novo_fabricante = {"nome": nome}
        data["fabricantes"].append(novo_fabricante)
        salvar_dados()
        st.success("Fabricante cadastrado com sucesso!")

def main():
    st.title("Otimizador de Corte de Chapas")
    menu = st.sidebar.selectbox("Menu", ["Cadastro de Chapas", "Cadastro de Fabricantes", "Cadastro de Clientes", "Cadastro de Peças", "Cadastro de Fitas", "Cadastro de Acessórios", "Plano de Corte"])
    
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
    elif menu == "Plano de Corte":
        calcular_plano_corte()

if __name__ == "__main__":
    try:
        import reportlab
    except ModuleNotFoundError:
        st.error("O módulo 'reportlab' não está instalado. Adicione 'reportlab' ao arquivo requirements.txt no Streamlit Cloud.")
    else:
        main()
