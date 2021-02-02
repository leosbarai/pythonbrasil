def triangle():
    print("********************************** ")
    print("           Triangulo! ")
    print("********************************** ")

    try:
        left_side = float(input("Informe o lado esquerdo do triângulo: "))
        right_side = float(input("Informe o lado direito do triângulo: "))
        base = float(input("Informe a base do triângulo: "))

        sum_left = left_side + right_side
        sum_right = right_side + base
        sum_base = base + left_side

        if sum_left < base or sum_right < left_side or sum_base < right_side:
            print('O valor informado não corresponde a um triângulo!')
        elif left_side == right_side and left_side == right_side and right_side == base:
            print('É um Triângulo Equilátero!')
        elif  left_side == right_side or left_side == right_side or right_side == base:
            print('É um Triângulo Isósceles!')
        else:
            print('É um Triângulo Escaleno!')

    except ValueError:
        print('Valor informado está inválido!')


if __name__ == "__main__":
    triangle()