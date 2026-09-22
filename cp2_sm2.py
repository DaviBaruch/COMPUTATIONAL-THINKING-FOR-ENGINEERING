#Guilherme Rodrigues de Souza RM573803, #Davi Baruch Gutierrez Varas RM572086

frutas = ["pera", "morango", "maça", "melancia"]
cores = ["preto", "laranja", "verde", "marrom"]

print("Escolha uma categoria:")
print("1 - Frutas")
print("2 - Cores")
opcao = int(input("Digite a opção: "))

if opcao == 1:
    lista_escolhida = frutas
elif opcao == 2:
    lista_escolhida = cores
else:
    print("Opção inválida! Selecionando 'Frutas' por padrão.")
    lista_escolhida = frutas

total_palavras = len(lista_escolhida)
print(f"\nA categoria possui {total_palavras} palavras.")
posicao = int(input("Escolha a posição da palavra: "))

indice = posicao - 1
if indice < 0 or indice >= total_palavras:
    print("Posição inválida! Selecionando a primeira palavra por padrão.")
    indice = 0

palavra_secreta = lista_escolhida[indice].lower()

palavra_descoberta = ["_"] * len(palavra_secreta)

tentativas = 6
print("\nVocê terá 6 tentativas para descobrir a palavra.")

while tentativas > 0 and "_" in palavra_descoberta:
    print(f"\nPalavra: {''.join(palavra_descoberta)}")
    print(f"Tentativas restantes: {tentativas}")

    letra = input("Digite uma letra: ").strip().lower()

    if letra in palavra_secreta:
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == letra:
                palavra_descoberta[i] = letra
    else:
        print("Você errou!")
        tentativas -= 1

if "_" not in palavra_descoberta:
    print(f"\nParabéns! Você descobriu a palavra: {palavra_secreta}")
else:
    print("\nSuas 6 tentativas terminaram.")
    print(f"A palavra era: {palavra_secreta}")