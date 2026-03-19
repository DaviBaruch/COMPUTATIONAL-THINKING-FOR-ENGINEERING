

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
print(dias * 24 * 60 * 60) + (horas * 60 * 60)


#7. Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.
salario = float(input("Digite o salario: "))
porcentagem = float(input("Digite a porcentagem de aumento: "))

aumento = salario * porcentagem / 100
novo_salario = salario + aumento

print("Aumento:", aumento)
print("Novo salario:", novo_salario)

print("Total em segundos:")
#8. Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.
preco = float(input("Digite o preço: "))
desconto = float(input("Digite o percentual de desconto: "))

valor_desconto = preco * desconto / 100
preco_final = preco - valor_desconto

print("Desconto:", valor_desconto)
print("Preço a pagar:", preco_final)
#9. Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
distancia = float(input("Digite a distancia: "))
velocidade = float(input("Digite a velocidade media: "))

tempo = distancia / velocidade

print("Tempo da viagem:", tempo, "horas")
#10. Escreva um programa que converta uma temperatura digitada em ºC em ºF. A fórmula para essa conversão é F = ((9 x C) / 5) + 32
c = float(input("Digite a temperatura em C: "))

f = (9 * c / 5) + 32

print("Temperatura em F:", f)

#11. Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado
km = float(input("Km percorridos: "))
dias = int(input("Dias alugados: "))

preco = dias * 60
preco = preco + km * 0.15

print("Preço a pagar:", preco)
#12
x = int(input("Digite x: "))
y = int(input("Digite y: "))

z = (x**2 + y**2) / (x - y)**2

print("Valor de z:", z)
#13
salario = float(input("Digite o salario: "))

novo = salario + salario * 0.35

print("Novo salario:", novo)

