#aprendendo while true dia 27/04 
#
soma = 0
quantidade = 0

while True:
   num = int(input("Digite um número inteiro: "))
   if num == 0:
     break
soma = soma + num
quantidade += 1
print("Quantidade de números digitados:",quantidade)
print("Soma =",soma)
print(f"Média = {(soma/quantidade):.2f}")

