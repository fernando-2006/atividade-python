# CONFIG
amountOfNames = 5


import sys

namesList = []

print("")
print("---BIBLIOTECA DE USUÁRIOS---")
print("Cadastre os nomes dos usuários.")
print("(Confirme com o campo vazio para PULAR um usuário)")
print("")

for i in range(amountOfNames):
    name = input(str(i + 1) + "/" + str(amountOfNames) + " Digite o nome: ")

    if not name == "":
        namesList.append(name)

print("")
print("Registro concluido com sucesso!")
print("Nomes registrados: ")
for name in namesList:
    print(name)
print("Número de nomes registrados: " + str(len(namesList)))


isSearchingActive = True
while (isSearchingActive):
    print("")
    print("---BIBLIOTECA DE USUÁRIOS---")
    print("Agora você pode pesquisar nomes registrados.")
    print("(Você pode interromper a pesquisa digitando \"PARAR\")")
    print("")

    nameToSearch = input("Digite o nome que deseja procurar: ")

    if nameToSearch == "PARAR":
        print("Sistema interrompido. Encerrando...")
        sys.exit()
    else:
        if nameToSearch in namesList:
            print("O nome " + nameToSearch + " foi encontrado!")
            print("Este é o " + str(namesList.index(nameToSearch) + 1) + "° nome registrado.")
        else:
            print("O nome " + nameToSearch + " não foi encontrado.")
        input("Pressone ENTER para prosseguir")