

check1 = float(input("Checkpoint 1: "))
check2 = float(input("Checkpoint 2: "))
media = (check1 + check2)/2
print(f"Média = {media:.1f}")

#Exercicios
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

#4. Faça um programa que peça dois números inteiros. Imprima a soma desses dois números na tela.
print("Coloque 2 números para somar")
numero1 = float(input("primeiro número: "))
numero2 = float(input("segundo número: "))
resultado_da_soma = numero1 + numero2
print(resultado_da_soma)
#5. Escreva um programa que leia um valor em metros e o exiba convertido em milímetros.
metro = 1
milimetros = metro * 1000
print(milimetros)


#6. Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos
dias = input("Dias:")
horas = int(input("Horas:"))
minutos = int(input("Minutos: "))
segundos = int(input(("Segundos: ")))
print(dias * 24 * 60 * 60) + (horas * 60 * 60) +


#7. Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.

#8. Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

#9. Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

#10. Escreva um programa que converta uma temperatura digitada em ºC em ºF. A fórmula para essa conversão é F = ((9 x C) / 5) + 32


#11. Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado