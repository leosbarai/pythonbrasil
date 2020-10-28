
def conversao():

    print("*********************************")
    print("  Imprimindo a média bimestral!")
    print("*********************************")

    print("Digite a quantidade de metros para conversão: ")
    metros = float(input())

    if metros > 0:
        print("Correspondem a {} centímetros!".format(metros*100))

if __name__ == "__main__":
    conversao()