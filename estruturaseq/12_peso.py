
def peso():
    print("************************************")
    print("          Peso ideal!")
    print("************************************")

    altura = float(input("Digite sua altura: "))

    peso = (72.2 * altura) - 58

    print("Seu peso ideal é : {}".format(round(peso, 2)))


if __name__ == "__main__":
    peso()