import streamlit as st
import pandas as pd
import json
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Inicialização dos dados (se não existirem)
try:
    with open('data.json', 'r') as f:
        data = json.load(f)
except FileNotFoundError:
    data = {'chapas': [], 'fabricantes': [], 'clientes': [], 'pecas': [], 'fitas': [], 'acessorios': []}

def salvar_dados():
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)

# Funções de cadastro (mantidas do código anterior)
def cadastrar_chapa():
    # ... (código de cadastro de chapa) ...

def cadastrar_fabricante():
    # ... (código de cadastro de fabricante) ...

def cadastrar_cliente():
    # ... (código de cadastro de cliente) ...

def cadastrar_peca():
    st.subheader("Cadastro de Peça")
    nome = st.text_input("Nome da Peça")
    dimensoes = st.text_input("Dimensões (LxC)")
    material = st.selectbox("Material", [c["nome"] for c in data["chapas"]])
    quantidade = st.number_input("Quantidade", min_value=1, value=1)

    col1, col2, col3 = st.columns(3)

    if col1.button("Salvar Peça"):
        nova_peca = {"nome": nome, "dimensoes": dimensoes, "material": material, "quantidade": quantidade}
        data["pecas"].append(nova_peca)
        salvar_dados()
        st.success("Peça cadastrada com sucesso!")
    if col2.button('Duplicar'):
        nova_peca = {"nome": nome + '(cópia)', "dimensoes": dimensoes, "material": material, "quantidade": quantidade}
        data["pecas"].append(nova_peca)
        salvar_dados()
        st.success("Peça duplicada com sucesso!")
    if col3.button('Apagar'):
        for peca in data['pecas']:
            if peca['nome'] == nome:
                data['pecas'].remove(peca)
                salvar_dados()
                st.success('Peça apagada com sucesso')
                break

    if st.button("Trocar Material em Grupo"):
        material_novo = st.selectbox('Selecione o novo material', [c["nome"] for c in data['chapas']])
        for peca in data['pecas']:
            if peca['nome'] == nome:
                peca['material'] = material_novo
                salvar_dados()
                st.success(f'Material alterado para {material_novo}')

    if len(data['pecas']) > 0:
        st.write('### Lista de peças cadastradas')
        df_pecas = pd.DataFrame(data['pecas'])
        st.dataframe(df_pecas)

def cadastrar_fita():
    # ... (código de cadastro de fita) ...

def cadastrar_acessorio():
    # ... (código de cadastro de acessório) ...

def calcular_plano_corte():
    st.subheader("Plano de Corte")
    if st.button("Calcular"):
        plano_de_corte = gerar_plano_de_corte()

        st.success("Plano de corte calculado!")

        buffer = io.BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)
        p.drawString(100, 750, "Plano de Corte")
        # Adicionar imagem do plano de corte ao PDF
        p.drawString(100, 700, str(plano_de_corte)) # exibir uma string para simular um plano de corte
        p.save()
        buffer.seek(0)

        st.download_button(label="Baixar PDF do Plano de Corte", data=buffer, file_name="plano_de_corte.pdf", mime="application/pdf")

def gerar_plano_de_corte():
    # Lógica de geração do plano de corte (substitua com sua implementação)
    st.write('plano de corte gerado')
    return 'Plano de corte gerado' # Exemplo de plano de corte

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
    main()
