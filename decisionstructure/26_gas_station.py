def gas_station():
    print("**********************************")
    print("         Posto de Gasolina!       ")
    print("**********************************")

    try:
        print("Escolha o combustível:")
        print("A-álcool")
        print("G-gasolina")
        fuel = input("--> ")
        validate(fuel)

        total = 0
        alcohol_price = 1.9
        gasoline_price = 2.5

        liters = float(input("Quantos litros deseja abastecer?: "))

        if fuel[0].upper() == 'A':
            if liters <= 20:
                value = alcohol_price * liters
                total = value - (value * 0.03)
            else:
                value = alcohol_price * liters
                total = value - (value * 0.05)
        elif fuel[0].upper() == 'G':
            if liters <= 20:
                value = gasoline_price * liters
                total = value - (value * 0.04)
            else:
                value = gasoline_price * liters
                total = value - (value * 0.06)

        print(f"Total do abastecimento: R$ {round(total, 2)}")

    except ValueError:
        print("Quantidade incorreta!")


def validate(answer):
    if (answer[0].upper() != 'A') and (answer[0].upper() != 'G'):
        print('Combustível inválido!')
        exit()


if __name__ == "__main__":
    gas_station()
