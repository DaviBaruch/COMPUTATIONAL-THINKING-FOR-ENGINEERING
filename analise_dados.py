import pandas as pd
import numpy as np

# Criando dados fictícios para análise
data = {
    'ID_Pedido': range(1001, 1011),
    'Produto': ['Notebook', 'Mouse', 'Teclado', 'Monitor', 'Mouse', 'Notebook', 'Teclado', 'Monitor', 'Mouse', 'Notebook'],
    'Quantidade': [1, 5, 2, 1, 3, 2, 1, 2, 10, 1],
    'Preco_Unitario': [5000, 150, 300, 1200, 150, 5000, 300, 1200, 150, 5000],
    'Data': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-02', '2023-01-03', '2023-01-04', 
                            '2023-01-05', '2023-01-05', '2023-01-06', '2023-01-07', '2023-01-08'])
}

df = pd.DataFrame(data)

# Calculando o faturamento total por linha
df['Total'] = df['Quantidade'] * df['Preco_Unitario']

# Salvando em CSV (caso queira baixar)
df.to_csv('vendas_teste.csv', index=False)

print("Dataset criado com sucesso!")
print(df.head())
print("\nFaturamento total por produto:")
print(df.groupby('Produto')['Total'].sum())
