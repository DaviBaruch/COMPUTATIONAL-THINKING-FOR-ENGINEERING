# x = 1
# print(x)
# x = 2
# print(x)
# x = 3
# print(x)

#1° exercicio

print("programa que vai de 1 a 100")
x = 1
while x <= 100:
    print(x)
    x += 1

#2° exercicio
x = 50
while x <= 100:
    print(x)
    x += 1

#3 exercicio

from time import sleep

#3° exercicio
x = 10
while x >= 0:
    print(x)
    x -= 1

print("!!!Fogo!!!")

#4° exercicio
fim = int(input("Escolha o ultimo número: "))

x = 0
while x <= fim:
    print(x)
    x += 1

fim = int(input("Escolha o ultimo número: "))
x = 1
while x <= fim:
    print(x)
    x += 1

#5° exercicio

x = 3
while x <= 30:
    print(x)
    x += 3

# 6° exercicio

fim = int(input(""))
num = int(input("Tabuada de: "))
x = 0
while x <= 10:
    print(f"{num} x {x} = {num * x}")
    x += 1

#exercicio extra

soma = 0
x = 0
while x < 3:
    x += 1
    check = float(input(f"Nota do Checkpoint {x}:"))
    soma += check
print(f"Media = {soma/x}")

#aprendendo while true dia 27/04 
#
soma = 0
quantidade = 0

while True:
   num = int(input("Digite um numero inteiro: "))
   if num == 0:
     break
soma = soma + num
quantidade += 1
print("Quantidade de números digitados:",quantidade)
print("Soma =",soma)
print(f"Média = {(soma/quantidade):.2f}")


while True:
    try:
        numero = int(input("Digite um número inteiro (0 sai): "))
        if numero == 0:
            break
    except Exception:
        print("Valor inválido! Digite novamente.")


codigo = int(input("Codigo do produto for 0 para exibir"))

#Exercicio 11 do PDF: Aula 04 GRAD_Computational Thinking for Engineering.pdf

#11. Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada. Utilize a tabela de códigos a seguir para obter o preço de cada produto: Seu programa deve exibir o total das compras depois que o usuário digitar 0. Qualquer outro código deve gerar a mensagem de erro “Código inválido”
apagar = 0
while True:
    codigo = int(input("Código do produto (0 para sair): "))
    preco = 0
    if codigo == 0:
        break
    elif codigo == 1:
        preco = 0.5
    elif codigo == 2:
        preco = 1
    elif codigo == 3:
        preco = 4
    elif codigo == 5:
        preco = 7
    elif codigo == 9:
        preco = 8
    else:
        print("Código inválido!")
    if preco != 0:
        quantidade = int(input("Quantidade: "))
    apagar = apagar+ (preco * quantidade)
    print(f"Total a pagar R${apagar:.2f}")