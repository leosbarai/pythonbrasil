
def fahrenheit():

    print("************************************")
    print("Convertendo Celsius para Fahrenheit!")
    print("************************************")

    celsius = float(input("Digite a temperatura em Celsius: "))

    fahr = (celsius * (9/5)) + 32

    print("A temperatura em Fahrenheit é: {}".format(round(fahr, 4)))


if __name__ == "__main__":
    fahrenheit()