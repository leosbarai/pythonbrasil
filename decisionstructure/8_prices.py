def prices():
    print("********************************** ")
    print("         Preços! ")
    print("********************************** ")

    try:
        print('Informe o preços dos produtos abaixo: ')
        product_a = float(input('Produto A: '))
        product_b = float(input('Produto B: '))
        product_c = float(input('Produto C: '))

        if (product_a < product_b) and (product_b < product_c):
            print(f'Você deve comprar o Produto A de R$ {product_a}!')
        elif product_b < product_c:
            print(f'Você deve comprar o Produto B de R$ {product_b}!')
        else:
            print(f'Você deve comprar o Produto C de R$ {product_c}!')
    except ValueError:
        print('Valor informado para o produto está incorreto, tente novamente!')

if __name__ == "__main__":
    prices()
