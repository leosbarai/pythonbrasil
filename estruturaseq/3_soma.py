
def soma():

    print("*********************************")
    print("     Imprimindo a soma!")
    print("*********************************")

    print("Digite um número: ")
    num1 = float(input())

    print("Digite outro número: ")
    num2 = float(input())

    print("A soma dos números é: {}".format(num1 + num2))

if __name__ == "__main__":
    soma()