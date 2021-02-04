def greengrocer():
    print("**********************************")
    print("             Fruteira!       ")
    print("**********************************")

    try:
        strawberry_kg = float(input('Informe o total de morangos em kg: '))
        apple_kg = float(input('Informe o total de maçãs em kg: '))

        strawberry_total = 0
        apple_total = 0

        if 0 < strawberry_kg <= 5:
            strawberry_total = strawberry_kg * 2.5
        else:
            strawberry_total = strawberry_kg * 2.2

        if 0 < apple_kg <= 5:
            apple_total = apple_kg * 1.8
        else:
            apple_total = apple_kg * 1.5

        total_price = strawberry_total + apple_total
        total_kg = strawberry_kg + apple_kg

        if total_kg > 8 or total_price > 25:
            total_price -= total_price * 0.1

        if total_price > 0:
            print(f'Total da compra R$ {total_price} e {total_kg} kgs')
        else:
            print('Nenhuma compra foi efetuada.')

    except ValueError:
        print('Valor incorreto informado no console.')


if __name__ == "__main__":
    greengrocer()
