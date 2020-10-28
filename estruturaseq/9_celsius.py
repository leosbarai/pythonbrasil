
def celsius():

    print("************************************")
    print("Convertendo Fahrenheit para Celsius!")
    print("************************************")

    fahr = float(input("Digite a temperatura em Fahrenheit: "))

    celsius = (fahr - 32) * (5/9)

    print("A temperatura em Celsius é: {}".format(round(celsius, 4)))

if __name__ == "__main__":
    celsius()