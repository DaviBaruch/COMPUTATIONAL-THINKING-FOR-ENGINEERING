# 1. Faça um programa que exiba seu nome na tela.
from tabnanny import check

nome = "Davi Baruch Gutierrez Varas"

print(nome)

print("\n")
# 2. Escreva um programa que exiba o resultado de 2a x 3b, em que a vale 3 e b vale 5

a = 3
b = 5

resultado = (a * 2) * (b * 5)
print(resultado)
# 3. Escreva um programa que calcule a soma de três variáveis e imprima o resultado na tela

print("\n")
c = 10
d = 20
e = 10

soma_de_tres_variaveis = c + d + e
print(soma_de_tres_variaveis)

idade = 19

print(10 // 3)


check1 = float(input("Checkpoint 1: "))
check2 = float(input("Checkpoint 2: "))
media = (check1 + check2)/2
print(f"Média = {media:.1f}")