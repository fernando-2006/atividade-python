# Ideia da recuperação:
# O aluno REPROVADO entra em recuperação se alcançar pelo menos a NOTA DE RECUPERAÇÃO (4 por padrão)

# CONFIG
gradesAmount = 3
approvationGrade = 6
recuperationGrade = 4


name = input("Digite o nome do aluno: ")
averageGrade = 0

for i in range(3):
    grade = float(input("Digite a nota " + str(i + 1) + ": "))
    averageGrade += grade

averageGrade /= gradesAmount

if averageGrade >= approvationGrade:
    print(name + " foi aprovado!")
    print("Média: " + str(averageGrade))
else:
    if averageGrade >= recuperationGrade:
        print(name + " ficou em recuperação!")
        print("Média: " + str(averageGrade))
    else:
        print(name + " foi reprovado...")
        print("Média: " + str(averageGrade))