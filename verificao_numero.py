intNumber = int(input("Digite um número inteiro: "))

isZero = intNumber == 0

if intNumber > 0:
    print("O número é POSITIVO.")
elif intNumber < 0:
    print("O número é NEGATIVO.")
elif isZero:
    print("O número é ZERO.")


if not isZero:
    if intNumber % 2 == 0:
        print("O número é PAR.")
    else:
        print("O número é ÍMPAR.")
else:
    print("É incerto se ZERO é ÍMPAR, ou nem ÍMPAR, nem PAR.")