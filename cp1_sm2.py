notas = []

cps = [
    "Checkpoint 1",
    "Checkpoint 2",
    "Checkpoint 3",
    "Sprint 1",
    "Sprint 2",
    "Global Solution"
]

for cp in cps:
    nota = float(input(f"{cp}: "))
    notas.append(nota)

menor_cp = min(notas[0:3])

media = ((notas[0] + notas[1] + notas[2] - menor_cp + notas[3] + notas[4]) / 4) * 0.4 + notas[5] * 0.6

print(f"Menor nota de checkpoint: {menor_cp:.1f}")
print(f"Média do 2º semestre: {media:.1f}")