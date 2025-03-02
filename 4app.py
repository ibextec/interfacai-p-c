import streamlit as st
import pandas as pd
import json
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import rectpack

# Função para carregar os dados do arquivo JSON
def carregar_dados():
    try:
        with open('data.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        # Dados iniciais caso o arquivo não exista
        return {
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

# Função para salvar os dados no arquivo JSON
def salvar_dados(data):
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)

# Funções de cadastro...
def cadastrar_chapa(data):
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
        salvar_dados(data)
        st.success("Chapa cadastrada com sucesso!")

def cadastrar_fabricante(data):
    st.subheader("Cadastro de Fabricante")
    nome = st.text_input("Nome do Fabricante")

    if st.button("Salvar Fabricante"):
        novo_fabricante = {"nome": nome}
        data["fabricantes"].append(novo_fabricante)
        salvar_dados(data)
        st.success("Fabricante cadastrado com sucesso!")

def cadastrar_cliente(data):
    st.subheader("Cadastro de Cliente")
    nome = st.text_input("Nome do Cliente")
    endereco = st.text_area("Endereço")
    telefone = st.text_input("Telefone")

    if st.button("Salvar Cliente"):
        novo_cliente = {"nome": nome, "endereco": endereco, "telefone": telefone}
        data["clientes"].append(novo_cliente)
        salvar_dados(data)
        st.success("Cliente cadastrado com sucesso!")

def cadastrar_peca(data):
    st.subheader("Cadastro de Peça")
    nome = st.text_input("Nome da Peça")
    dimensoes = st.text_input("Dimensões (LxC)")
    material = st.selectbox("Material", [c["nome"] for c in data["chapas"]])
    quantidade = st.number_input("Quantidade", min_value=1, value=1)

    col1, col2, col3 = st.columns(3)

    if col1.button("Salvar Peça"):
        nova_peca = {"nome": nome, "dimensoes": dimensoes, "material": material, "quantidade": quantidade}
        data["pecas"].append(nova_peca)
        salvar_dados(data)
        st.success("Peça cadastrada com sucesso!")
    if col2.button('Duplicar'):
        nova_peca = {"nome": nome + '(cópia)', "dimensoes": dimensoes, "material": material, "quantidade": quantidade}
        data["pecas"].append(nova_peca)
        salvar_dados(data)
        st.success("Peça duplicada com sucesso!")
    if col3.button('Apagar'):
        for peca in data['pecas']:
            if peca['nome'] == nome:
                data['pecas'].remove(peca)
                salvar_dados(data)
                st.success('Peça apagada com sucesso')
                break

    if st.button("Trocar Material em Grupo"):
        material_novo = st.selectbox('Selecione o novo material', [c["nome"] for c in data['chapas']])
        for peca in data['pecas']:
            if peca['nome'] == nome:
                peca['material'] = material_novo
                salvar_dados(data)
                st.success(f'Material alterado para {material_novo}')

    if len(data['pecas']) > 0:
        st.write('### Lista de peças cadastradas')
        df_pecas = pd.DataFrame(data['pecas'])
        st.dataframe(df_pecas)

def cadastrar_fita(data):
    st.subheader("Cadastro de Fita")
    nome = st.text_input("Nome da Fita")
    espessura = st.number_input("Espessura (mm)")
    cor = st.text_input("Cor")

    if st.button("Salvar Fita"):
        nova_fita = {"nome": nome, "espessura": espessura, "cor": cor}
        data["fitas"].append(nova_fita)
        salvar_dados(data)
        st.success("Fita cadastrada com sucesso!")

def cadastrar_acessorio(data):
    st.subheader("Cadastro de Acessório")
    nome = st.text_input("Nome do Acessório")
    descricao = st.text_area("Descrição")
    preco = st.number_input("Preço")

    if st.button("Salvar Acessório"):
        novo_acessorio = {"nome": nome, "descricao": descricao, "preco": preco}
        data["acessorios"].append(novo_acessorio)
        salvar_dados(data)
        st.success("Acessório cadastrado com sucesso!")

def calcular_plano_corte(data):
    st.subheader("Plano de Corte")
    if st.button("Calcular"):
        plano_de_corte = gerar_plano_de_corte(data)

        st.success("Plano de corte calculado!")

        buffer = io.BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)
        p.drawString(100, 750, "Plano de Corte")
        # Adicionar imagem do plano de corte ao PDF
        p.drawString(100, 700, str(plano_de_corte)) # exibir uma string para simular um plano de corte
        p.save()
        buffer.seek(0)

        st.download_button(label="Baixar PDF do Plano de Corte", data=buffer, file_name="plano_de_corte.pdf", mime="application/pdf")

def gerar_plano_de_corte(data):

    # Função exemplo para calcular o plano de corte (substitua pela sua lógica)
    st.write('plano de corte gerado')
    return 'Plano de corte gerado
