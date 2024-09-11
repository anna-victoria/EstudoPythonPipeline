import streamlit as st
from contrato import Vendas
from contrato import ProdutoEnum
from datetime import datetime, time
from pydantic import ValidationError


import contrato
from database import salvar_no_postgres

def main():
    st.title("Sistema de CRM e Vendas")
    email = st.text_input("Email do vendedor")
    data = st.date_input("Data da compra", datetime.now())
    hora = st.time_input("Hora da compra", value=time(9, 0))  # Valor padrão: 09:00
    valor = st.number_input("Valor da venda")
    quantidade = st.number_input("Quantidade de produtos", min_value=1, step=1)
    produto = st.selectbox("Selecione o produto vendido", ["Produto 1" , "Produto 2", "Produto 3"]) 
    
    if st.button("Salvar"):
        
        # Fazer o try-except para tratar os erros de validação.
        # Isso é importante para que o usuário saiba o que está errado, e possa corrigir o erro.
        
        try:        
            data_hora = datetime.combine(data, hora)
            # Esse data_hora é um objeto datetime que combina a data e a hora que o usuário inseriu
            
            venda = Vendas(email=email, data=data, hora=hora, valor=valor, quantidade=quantidade, produto=produto) 
            # Aqui, estamos criando uma instância da classe Vendas, que foi definida no arquivo contrato.py
            
            salvar_no_postgres(venda)
        
        except ValidationError as e:
            st.error(f"Erro de validação: {e}")
        
       
if __name__ == '__main__':
    main()
# esse if é para garantir que o código só será executado se o arquivo for 
# executado diretamente, e não se for importado por outro arquivo
# esse __name__ é uma variável que o Python cria para cada arquivo, e ela
# é igual a "__main__" se o arquivo for executado diretamente
