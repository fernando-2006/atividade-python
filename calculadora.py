# Pegue 2 números e permita soma, subtração, multiplicação e divisão.

# Ideia: Usarei uma função nova chamada dynamicInput ao invés da input normal
# a dynamicInput para o programa se for digitado "PARAR"

import sys

isProgramRunning = True

# Além de chamar o input, interrompe a execução se receber "PARAR"
def dynamicInput(receivingInput):
    inputResponse = input(receivingInput)

    if inputResponse == "PARAR":
        print("Sistema interrompido. Encerrando...")
        sys.exit()
    else:
        return inputResponse


while (isProgramRunning):
    print("")
    print("---Calculadora---")
    print("Faça cálculos com processos aritméticos básicos!")
    print("Em QUALQUER campo, digite \"PARAR\" para interromper a execução do programa.")
    print("")

    num1 = float(dynamicInput("Digite o primeiro número: "))
    num2 = float(dynamicInput("Digite o segundo número: "))

    print("")
    print("Números digitados: " + str(num1) + " e " + str(num2))
    print("Digite o número relativo ao processo aritmético escolhido para usá-lo na conta.")
    print("> 1. Adição")
    print("> 2. Subtração")
    print("> 3. Multiplicação")
    print("> 4. Divisão")
    
    operation = input("Operação a ser usada: ")
    if operation == "1":
        print("")
        print(str(num1) + " + " + str(num2) + " = " + str(num1 + num2))
    elif operation == "2":
        print("")
        print(str(num1) + " - " + str(num2) + " = " + str(num1 - num2))
    elif operation == "3":
        print("")
        print(str(num1) + " x " + str(num2) + " = " + str(num1 * num2))
    elif operation == "4":
        print("")
        print(str(num1) + " / " + str(num2) + " = " + str(num1 / num2))
    else:
        print("Operação inválida.")

    print("")
    print("Execução concluída.")
    input("Digite \"PARAR\" para encerrar, ou pressione qualquer tecla para continuar: ")