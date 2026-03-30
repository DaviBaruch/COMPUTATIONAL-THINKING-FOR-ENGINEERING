#If condicionais
from segunda_aula import salario

# exercicios

# 1. Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$5 por km acima de 80km/h

velocidade = float(input("Qual foi sua velocidade maxima? "))

if velocidade > 80:
     multa = (velocidade - 80) * 5
     print("vc recebeu uma multa")
     print(f"valor da multa R${multa:.2f}.",)

else:
    print("Velocidade dentro do limite")


#2. Escreva um programa que leia três números e que imprima o maior e o menor
a = int(input("Digite um número: "))
b = int(input("Digite um número: "))
c = int(input("Digite um número: "))

maior = a
if b >= a and b >= c:
    maior = b
if c >= a and c >=b:
    maior = c

menor = a
if b <= a and b <= c:
    menor = b
if c <= a and c <=b:
    menor = c
print(f"Maior = {maior}")
print(f"Menor = {menor}")

# 3.Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para inferiores ou iguais, de 15%.

salario = float(input("Salário = R$"))

if salario > 1250:
    aumento = salario *0.1
else:
    aumento = salario * 0.15

print(f"Aumento de R${aumento:.2f}")

# 4. Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200 km e R$ 0,45 para viagens mais longas
distancia = float(input("Escreva a distância em km:"))

if distancia <= 200 :
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f"O preço da passagem R${preco:.2f}.")

#5. Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você deve poder calcular soma, subtração, multiplicação e divisão. Exiba o resultado da operação solicitada.

print("Calculadora. Escolha os números que você quer calcular")
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo: "))

if operacao == "+":
    print(a + b)
elif operacao == "-":
    print(a - b)
elif operacao == "*":
    print(a * b)
elif operacao == "/":
    print(a / b)

