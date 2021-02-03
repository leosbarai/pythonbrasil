def even_odd():
    print("********************************** ")
    print("             Saque! ")
    print("********************************** ")

    try:
        number = int(input('Informe um número inteiro: '))

        if number % 2 == 0:
            print(f'{number} é par!')
        else:
            print(f'{number} é ímpar!')

    except ValueError:
        print('Somente números inteiros são válidos!')


if __name__ == "__main__":
    even_odd()
