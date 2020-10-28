
def calculos():

    print("************************************")
    print("            Cálculos!")
    print("************************************")

    num1 = int(input("Digite um número inteiro: "))
    num2 = int(input("Digite um outro inteiro: "))
    num3 = float(input("Digite um número real: "))

    dobro = (num1 * 2) + (num2 / 2)
    triplo = (num1 * 3) + num3
    cubo = num3**3

    print("Dobro do primeiro número com a metade do segundo: {}".format(dobro))
    print("Soma do triplo do primeiro com o terceiro: {}".format(triplo))
    print("Cubo do terceiro: {}".format(cubo))


if __name__ == "__main__":
    calculos()