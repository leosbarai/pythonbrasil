def payment():
    print("********************************** ")
    print("             Payment! ")
    print("********************************** ")

    try:
        value = float(input('Informe seu salário hora: '))
        hour = float(input('Informe as horas trabalhadas no mês: '))

        gross_total = round(value * hour, 2)
        union_tax = 3
        fgts_tax = 11

        if gross_total <= 900.0:
            ir_tax = 0
            ir = 0.00
        elif gross_total <= 1500.0:
            ir_tax = 5
            ir = round((gross_total * ir_tax)/100)
        elif gross_total <= 2500.0:
            ir_tax = 10
            ir = round((gross_total * ir_tax) / 100)
        else:
            ir_tax = 20
            ir = round((gross_total * ir_tax) / 100)

        union = round((gross_total * union_tax)/100, 2)
        fgts = round((gross_total * fgts_tax)/100, 2)
        reduction = union + ir
        liquid_total = gross_total - reduction

        print(f'Salário bruto: R$ ({value} * {hour})   : R$ {gross_total}')
        print(f'(-) IR ({ir_tax}%)                       : R$ {ir}')
        print(f'(-) Sindicato ({union_tax}%)                 : R$ {union}')
        print(f'FGTS ({fgts_tax}%)                         : R$ {fgts}')
        print(f'Total de descontos                 : R$ {reduction}')
        print(f'Salário Liquido                    : R$ {liquid_total}')
        
    except ValueError:
        print('Valor informado para o produto está incorreto, tente novamente!')


if __name__ == "__main__":
    payment()