import streamlit as st
import pandas as pd
import cadastro
import calculos
import layout
import exportacao
import json

# Carregar dados (se existirem)
try:
    with open('data.json', 'r') as f:
        data = json.load(f)
except FileNotFoundError:
    data = {'chapas': [], 'fabricantes': [], 'clientes': [], 'pecas': [], 'fitas': [], 'acessorios': []}

def salvar_dados():
    with open('data.json', 'w') as f:
        json.dump(data, f)

def main():
    st.title('Otimizador de Corte de Chapas')

    menu = st.sidebar.selectbox('Menu', ['Cadastro', 'Cálculo', 'Layout', 'Exportação'])

    if menu == 'Cadastro':
        cadastro.cadastro(data)
        salvar_dados()

    elif menu == 'Cálculo':
        calculos.calculos(data)

    elif menu == 'Layout':
        layout.layout(data)

    elif menu == 'Exportação':
        exportacao.exportacao(data)

if __name__ == '__main__':
    main()
