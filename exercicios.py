from segunda_aula import desconto

print("Olá Davi Baruch, você tem 19 anos anos.")

operacao = input("Escolha a operação que você deseja(+ - * /")

print("digite os números pra calcular")
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

numero = int(input("coloque um número para ser transformado ao quadrado: "))
print(numero ** 2)

nota1 = int(input("Digite sua primeira nota: "))
nota2 = int(input("Digite sua segunda nota: "))
media = (nota1 + nota2) / 2
if media >= 6:
    print("Você foi aprovado")
else:
    print("Você foi reprovado")

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Maior de idade")

else:
    print("Menor de idade")

numeros = int(input("Digite um numero para verificar se é par ou impar: "))

if numeros % 2 == 0:
    print("Par")
else:
    print("Impar")

# Peça o preço de um produto. Se for maior que 100 → desconto 10% Senão → desconto 5%

preco = int(input("Qual foi o valor do produto?: "))
if preco >= 100:
    print(f"você recebeu um desconto de 10%")
else:
    print(f"Você recebeu um desconto de 5%")
desconto_5 = preco - (preco * 0.05)
desconto_10 = preco - (preco * 0.10)