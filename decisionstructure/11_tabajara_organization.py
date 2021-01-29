def tabajara():
    print("********************************** ")
    print("      Tabajara Organization! ")
    print("********************************** ")

    try:
        salary = float(input('Informe seu salário: '))

        if salary <= 280.00:
            perc = 20
            increase = round((salary * perc)/100, 2)
        elif salary <= 750.00:
            perc = 15
            increase = round((salary * perc)/100, 2)
        elif salary <= 1500.00:
            perc = 10
            increase = round((salary * perc)/100, 2)
        else:
            perc = 5
            increase = round((salary * perc)/100, 2)

        new_salary = round(salary + increase, 2)

        print(f'Salário base: R$ {salary}')
        print(f'Percentual de aumento aplicado: {perc}%')
        print(f'Valor do aumento: R$ {increase}')
        print(f'Novo salário: R$ {new_salary}')

    except ValueError:
        print('Valor digitado incorreto!')


if __name__ == "__main__":
    tabajara()
