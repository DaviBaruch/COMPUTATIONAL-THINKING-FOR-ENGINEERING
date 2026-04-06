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