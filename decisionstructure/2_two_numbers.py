def numbers():
    print("**********************************")
    print("      Exibe o Maior Número!")
    print("**********************************")

    number_one = input("Informe o primeiro número: ")
    number_two = input("Informe o segundo número: ")

    if number_one.isdigit() and number_two.isdigit():
        if number_one > number_two:
            print(f"{number_one} é maior que {number_two}!")
        elif number_one < number_two:
            print(f"{number_two} é maior que {number_one}!")
        else:
            print("Os números são iguais")
    else:
        print("Valor digitado não é um número!")


if __name__ == "__main__":
    numbers()
