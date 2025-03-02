import streamlit as st

def cadastro(data):
    cadastro_opcao = st.selectbox('Cadastrar', ['Chapas', 'Fabricantes', 'Clientes', 'Peças', 'Fitas', 'Acessórios'])

    if cadastro_opcao == 'Chapas':
        # Formulário para cadastro de chapas
        st.subheader('Cadastro de Chapas')
        # Implemente os campos necessários

        if st.button('Salvar Chapa'):
            # Adicione a chapa aos dados
            pass

    # Outros cadastros...
