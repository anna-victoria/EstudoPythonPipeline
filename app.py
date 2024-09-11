import streamlit as st
import contrato
from datetime import datetime, time

def main():
    st.title("Sistema de CRM e Vendas - Frontend")
    email = st.text_input("Email do vendedor")
    data = st.date_input("Data da compra", datetime.now())
    hora = st.time_input("Hora da compra", value=time(9, 0))  # Valor padrão: 09:00
    valor = st.number_input("Valor da venda")
    quantidade = st.number_input("Quantidade de produtos")
    produto = st.selectbox("Selecione o produto vendido", ["Zapflow com Gemini" , "Zapflow com ChatGPT", "Zapflow com Lhama"]) 
    
    if st.button("Salvar"):
        data_hora = datetime.combine(data, hora)
        st.write("Dados da venda:")
        st.write(f"Email do vendedor: {email}")
        st.write(f"Data da venda: {data}")
        st.write(f"Hora da venda: {hora}")
        st.write(f"Valor da venda: {valor}")
        st.write(f"Quantidade de produtos: {quantidade}")
        st.write(f"Produto vendido: {produto}")
        
       
if __name__ == '__main__':
    main()
# esse if é para garantir que o código só será executado se o arquivo for 
# executado diretamente, e não se for importado por outro arquivo
# esse __name__ é uma variável que o Python cria para cada arquivo, e ela
# é igual a "__main__" se o arquivo for executado diretamente
