
def peso():
    print("************************************")
    print("          Peso ideal!")
    print("************************************")

    altura = float(input("Digite sua altura: "))
    sexo = input("Digite o sexo M ou F: ")

    if sexo[0].upper() == 'M':
        peso = (72.2 * altura) - 58
        print("Seu peso ideal é : {}".format(round(peso, 2)))
    elif sexo[0].upper() == 'F':
        peso = (62.1 * altura) - 44.7
        print("Seu peso ideal é : {}".format(round(peso, 2)))
    else:
        print("Sexo informado é inválido!")

if __name__ == "__main__":
    peso()