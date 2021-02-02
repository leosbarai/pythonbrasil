def number():
    print("********************************** ")
    print("            Dezenas! ")
    print("********************************** ")


    number = input('Digite um número de 1 a 999: ')

    if number.isdigit():
        if len(number) == 3:
            print(f'{number} = {hundreds(number[0])}, {tens(number[1])} e {unities(number[2])}')
        elif len(number) == 2:
            print(f'{number} = {tens(number[0])} e {unities(number[1])}')
        elif len(number) == 1:
            print(f'{number} = {unities(number[0])}')
        else:
            print('Número inválido')
    else:
        print('Os valores digitados estão incorretos!')


def unities(number):
    if number <= '1':
        return f'{number} unidade'
    else:
        return f'{number} unidades'


def tens(number):
    if number <= '1':
        return f'{number} dezena'
    else:
        return f'{number} dezenas'


def hundreds(number):
    if number <= '1':
        return f'{number} centena'
    else:
        return f'{number} centenas'


if __name__ == "__main__":
    number()
