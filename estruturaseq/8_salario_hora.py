
def salario():

    print("*********************************")
    print("     Cálculo salário/hora!")
    print("*********************************")

    valor = float(input("Informe o valor da hora: "))
    horas = float(input("Informe as horas trabalhadas: "))

    print("Seu salário do mês é: {}".format(round(valor * horas, 2)))

if __name__ == "__main__":
    salario()