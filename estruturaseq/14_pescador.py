
def pescador():
    print("************************************")
    print("     João Papo-de-Pescador")
    print("************************************")

    peso = float(input("Informe o peso total dos peixes: "))

    if peso > 50:
        excesso = peso - 50
        multa = excesso * 4.0
        print("A multa pelo peso excedente de {} é no valor de {}".format(round(excesso, 2), round(multa, 2)))
    else:
        print("Peso dentro do estabelecido pelo regulamento.")

if __name__ == "__main__":
    pescador()