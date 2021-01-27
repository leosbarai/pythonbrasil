def major_minor():
    print("********************************** ")
    print("         Maior e Menor! ")
    print("********************************** ")

    try:
        number_one = float(input('Informe a 1ª número: '))
        number_two = float(input('Informe a 2ª número: '))
        number_three = float(input('Informe a 3º número: '))

        if (number_one > number_two) and (number_one > number_three):
            major = number_one
        elif number_two > number_three:
            major = number_two
        else:
            major = number_three

        if (number_one < number_two) and (number_one < number_three):
            minor = number_one
        elif number_two < number_three:
            minor = number_two
        else:
            minor = number_three

        print(f'O maior número é o {major} e o menor é o {minor}')

    except ValueError:
        print('O valor informado não é um número!')


if __name__ == "__main__":
    major_minor()
