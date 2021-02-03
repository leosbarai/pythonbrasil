import math

def alternatives():
    print("**********************************")
    print("         Alternativas!            ")
    print("**********************************")

    try:
        number = float(input('Digite um número: '))

        print('Escolha uma das alternativas para análise: ')
        print('a. par ou ímpar;')
        print('b. positivo ou negativo;')
        print('c. inteiro ou decimal')
        choice = input('-> ')

        if choice.upper() == 'A':
            odd_even(number)
        elif choice.upper() == 'B':
            positive_negative(number)
        elif choice.upper() == 'C':
            int_dec(number)
        else:
            print('Alternativa incorreta!')

    except ValueError:
        print('Digite um número inteiro ou decimal!')


def odd_even(number):
    if number % 2 == 0:
        print(f'Número informado é par!')
    else:
        print(f'Número informado é ímpar!')


def positive_negative(number):
    if number >= 0:
        print(f"O número informado é positivo!")
    else:
        print(f"O número informado é negativo!")


def int_dec(number):
    if math.ceil(number) > number:
        print('Número decimal!')
    else:
        print('Número inteiro!')


if __name__ == "__main__":
    alternatives()
