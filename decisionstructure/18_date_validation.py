def date():
    print("********************************** ")
    print("      Validação das datas! ")
    print("********************************** ")

    try:
        day = int(input("Informe o dia: "))
        month = int(input("Informe o mês: "))
        year = int(input("Informe o ano: "))
        valid_date = False

        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            if day <= 31:
                valid_date = True
        elif month == 4 or month == 6 or month == 9 or month == 11:
            if day <= 30:
                valid_date = True
        elif month == 2:
            if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
                if day <= 29:
                    valid_date = True
            elif day <= 28:
                valid_date = True

        if valid_date:
            print(f"A data {day}/{month}/{year} é válida!")
        else:
            print(f"A data {day}/{month}/{year} é inválida!")

    except ValueError:
        print('Valores informados estão incorretos!')


if __name__ == "__main__":
    date()