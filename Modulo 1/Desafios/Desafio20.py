import random

alunos = []
i = 0

while i <= 3:
    alunos.append(input("Digite o nome do aluno: "))
    i += 1

print("A ordem de apresentação será: ")

random.shuffle(alunos)

i = 0
while i <= 3:
    print(f"{alunos[i]}")
    i += 1
