def equation():
    print("********************************** ")
    print("      Equação de 2º Grau! ")
    print("********************************** ")

    try:
        print('Para a resolução da fórmula ax2 + bx + c, informe os valores de')
        a = int(input('a: '))
        b = int(input('b: '))
        c = int(input('c: '))

        if a == 0:
            print('Não é equação de segundo grau!')
            exit()

        delta = (b * b) - (4 * a * c)

        if delta < 0:
            print('Equação não possui raizes reais!')
        elif delta == 0:
            print('A equação possui apenas uma raiz real!')
        else:
            print('A equação possui duas raiz reais!')
            

    except ValueError:
        print('Valores informados para a equação não estão corretos!')


if __name__ == "__main__":
    equation()
