#listas e matrizes

idade_familia = [
    [20, 43, 42, 12],
    [22, 46, 40, 17]]

print(idade_familia[1][0])

#Usando em um exemplo
#Davi
#RM572086   
#9.0
#1ECR
lista_alunos = [
    {"Nome": "Davi", 
     "RM": "572086", 
     "Nota": 9.0, 
     "Turma": "1ECR"},

   {"Nome": "Gabi",
    "RM": "572089", 
    "Nota": 8.0, 
    "Turma": "1ECR"},
]


print(lista_alunos[0]["Nome"], lista_alunos [0]["Nota"])
for aluno in lista_alunos:
    print(aluno["Nome"], aluno["Nota"] )

#Desafio:
#Crie um dicionario para representar um sensor contendo: id, tipo, valor e unidade;
#todas as informação dos sensores;
#Alternar o valor da leitura;
#informar ATENÇÂO caso a nova temperatura seja maior que 37°C;
#Caso contrario, infomar NORMAL.

sensor = {"id": 1,
            "tipo": "Temperatura",
            "valor": 36.6,
            "unidade": "°C"
            }

print("Informações do sensor:")
print(f"ID: {sensor['id']}")
print(f"Tipo: {sensor['tipo']}")
print(f"Valor: {sensor['valor']}{sensor['unidade']}")
print(f"Unidade: {sensor['unidade']}")

# Alternar o valor da leitura
nova_temperatura = float(input("\nDigite a nova temperatura: "))

sensor["valor"] = nova_temperatura

print(f"\nNova temperatura: {sensor['valor']}{sensor['unidade']}")

# Verificar temperatura
if sensor["valor"] > 37:
    print("ATENÇÃO")
else:
    print("NORMAL")