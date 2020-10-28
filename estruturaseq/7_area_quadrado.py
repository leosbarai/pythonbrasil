
def area():

    print("*********************************")
    print("  Imprimindo o área do quadrado!")
    print("*********************************")

    print("Informe o tamanho do lado do quadrado em centímetros:")
    lado = float(input())
    lado = lado**2

    print("A área do quadrado é {}".format(lado))

    print("O dobro dá área do quadrado é {}".format(lado*2))

if __name__ == "__main__":
    area()