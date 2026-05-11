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
    #print(f"Média = {soma/4}")
    #print(f"Média = {soma/[x]}")
    print(f"Média = {soma/len(notas_check)}")


# Sei lá o que ela quer fazer aqui eu perdi essa parte kkk ela quer inputar a nota 

notas_check = []
soma = 0
x = 0
quant = int(input("Quantidade de alunos"))
while True:
    nota = float(input(f"Checkpoint aluno {x+1} = "))
    notas_check.append(nota)
    soma += notas_check[x]
    x += 1
    if quant == len(notas_check):
        break
    print(f"Média = {soma/len(notas_check)}")

#algumas build-ins no python

#sort ordena a lista em ordem crescente e usando o sort(reverse=True) fica decrescente
#min() mostra a menor nota da lista, tuplas dicionarios e strings
#max() mostra a maior nota da lista, tuplas dicionarios e strings
#abs() Retorna o valor absoluto de um número.
