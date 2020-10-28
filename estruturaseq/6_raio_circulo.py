
def raio():

    print("*********************************")
    print("  Imprimindo o raio do círculo!")
    print("*********************************")

    print("Informe o raio do círculo em centímetros: ")
    raio = float(input())
    raio = raio**2
    pi = 3.1415926535898

    print("A área do círculo é: {}".format(round((raio*pi), 2)))

if __name__ == "__main__":
    raio()