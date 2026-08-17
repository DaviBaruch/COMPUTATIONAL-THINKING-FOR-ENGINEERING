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