def major():
    print("********************************** ")
    print("         Maior Número! ")
    print("********************************** ")

    try:
        number_one = float(input("Informe a 1ª número: "))
        number_two = float(input("Informe a 2ª número: "))
        number_three = float(input("Informe a 3º número: "))

        if (number_one > number_two) and (number_one > number_three):
            print(f"O {number_one} é o maior número.")
        elif number_two > number_three:
            print(f"O {number_two} é o maior número.")
        else:
            print(f"O {number_three} é o maior número.")

    except ValueError:
        print("O valor informado não é um número!")


if __name__ == "__main__":
    major()
