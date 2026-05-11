#listas
compras_super = ["Feijão", "Arroz", "Leite", "Biscoito"]
compras_super[3] = "Bolacha"
print(compras_super)

#media de notas

notas_check = [5, 8, 10, 7]
soma = 0
x = 0
while x < 4:
    soma = soma + notas_check[x]
    x = x + 1

    print(f"Média = {soma/4}")
    