
def media():

    print("*********************************")
    print("  Imprimindo a média bimestral!")
    print("*********************************")

    print("Informe a nota do 1º bimestre: ")
    nota1 = float(input())

    print("Informe a nota do 2º bimestre: ")
    nota2 = float(input())

    print("Informe a nota do 3º bimestre: ")
    nota3 = float(input())

    print("Informe a nota do 4º bimestre: ")
    nota4 = float(input())

    media = nota1 + nota2 + nota3 + nota4

    if media > 0:
        media /= 4
        print("Sua média é {}".format(media))
    else:
        print("Sua média é 0")

if __name__ == "__main__":
    media()