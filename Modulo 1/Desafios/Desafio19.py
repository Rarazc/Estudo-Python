import random

alunos = []
i = 0

while i <= 3:
    alunos.append(input("Digite o nome do aluno: "))
    i += 1

sorteado = random.randint(0,3)

print(f"O aluno sorteado foi {alunos[sorteado]}")