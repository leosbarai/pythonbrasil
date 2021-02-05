def tabajara():
    print("**********************************")
    print("      Tabajara Organization!      ")
    print("**********************************")

    try:
        print('Escolha a carne:')
        print('1. Filé Duplo')
        print('2. Alcatra')
        print('3. Picanha')
        option = int(input('-> '))

        if 1 <= option <= 3:
            kgs = float(input('Informe a quantidade em quilos: '))

            if kgs <= 0:
                print('Quantidade inválida!')
                exit()

            gross_total = 0
            net_total = 0
            discount = 0

            if option == 1:
                if kgs <= 5:
                    gross_total = kgs * 4.9
                else:
                    gross_total = kgs * 5.8
            elif option == 2:
                if kgs <= 5:
                    gross_total = kgs * 5.9
                else:
                    gross_total = kgs * 6.8
            elif option == 3:
                if kgs <= 5:
                    gross_total = kgs * 6.9
                else:
                    gross_total = kgs * 7.8

            payment = input('O pagamento será efetuado com o cartão Tabajara? [S/N]: ')

            if payment[0].upper() == 'S':
                discount = gross_total * 0.05
                net_total = gross_total - discount
            else:
                net_total = gross_total

            print("*** CUPOM FISCAL ***")

            if option == 1:
                print('1. Filé Duplo')
            elif option == 2:
                print('2. Alcatra')
            else:
                print('3. Picanha')

            print(f'Quantidade: {round(kgs, 2)}')
            print(f'Total bruto: R$ {round(gross_total, 2)}')

            if payment[0].upper() == 'S':
                print('Cartão Tabajara: S')
                print(f'Valor do desconto: R$ {round(discount, 2)}')
            else:
                print('Cartão Tabajara: N')
                print(f'Valor do desconto: R$ 0.0')

            print(f'Total a pagar: R$ {round(net_total, 2)}')
        else:
            print('Opção incorreta!')

    except ValueError:
        print('Valor incorreto!')


if __name__ == '__main__':
    tabajara()
