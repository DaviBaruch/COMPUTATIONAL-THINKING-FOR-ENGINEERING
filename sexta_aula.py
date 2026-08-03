#Repetição - for aula 6

compras = ["arroz", "feijão", "frango", "batata"]
produto = input("digite o nome do produto:")
for i in compras:
    if i == produto:
        print("Produto encontrado")
        break
else:
    print("Produto não encontrado")

#