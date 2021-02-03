def positive():
    print("**********************************")
    print("  Número é positivo ou negativo!")
    print("**********************************")

    try:
        number = float(input("Informe um número positivo ou negativo: "))

        if number >= 0:
            print(f"O número {number} é positivo!")
        else:
            print(f"O número {number} é negativo!")

    except ValueError:
        print("O valor informado não é um número!")

if __name__ == "__main__":
    positive()