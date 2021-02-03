import math

def int_dec():
    print("********************************** ")
    print("             Saque! ")
    print("********************************** ")

    try:
        number = float(input('Informe um número: '))

        if math.ceil(number) > number:
            print('Número decimal!')
        else:
            print('Número inteiro!')

    except ValueError:
        print('Digite apenas números inteiros ou decimais!')


if __name__ == '__main__':
    int_dec()
