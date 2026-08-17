#Repetição - for aula 6

compras = ["arroz", "feijão", "frango", "batata"]
produto = input("digite o nome do produto:")
for i in compras:
    if i == produto:
        print("Produto encontrado")
        break
else:
    print("Produto não encontrado")

#Usando Range
for i in range(10):
    print(i)


for i in range(5, 8):
    print(i)

#exercicios
# 1. Altere o programa do exemplo anterior de formar a imprimir o menor elemento da lista.

