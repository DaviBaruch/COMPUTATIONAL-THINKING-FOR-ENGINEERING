#nome = (input("Digite seu nome: "))
#idade = int(input("Digite sua idade: "))

#print(f"Olá {nome}, você tem {idade} anos.")

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


