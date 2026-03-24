#Desenvolver um programa em Python que:
#• Receba as notas do aluno
#• Identifique corretamente a menor nota entre os checkpoints
#• Calcule as médias conforme as regras estabelecidas
#• Exiba os resultados com a formatação correta

cp1 = float(input("Nota Checkpoint 1: "))
cp2 = float(input("Nota Checkpoint 2: "))
cp3 = float(input("Nota Checkpoint 3: "))
sp1 = float(input("Nota Sprint 1 "))
sp2 = float(input("Nota Sprint 2: "))
gs = float(input("Global Solution: "))

#menor nota dos 3 ckeckpoints

menor_Checkpoint = cp1
if cp2 <= cp1 and cp2 <= cp3:
 menor_Checkpoint = cp2
if cp3 <= cp2 and cp3 <= cp1:
 menor_Checkpoint = cp3
print(f"a menor nota do ckeckpoint é:{menor_Checkpoint:.1f} ")

media = ((cp1 + cp2 + cp3 - menor_Checkpoint + sp1 + sp2) / 4 ) * 0.4 + gs * 0.6
peso = media * 0.4

print(f"A média é{media:.1f} ")
print(f"media do aluno com peso do semestre é: {peso:.1f}")