def leap():
    print("********************************** ")
    print("      Verifica ano bissexto! ")
    print("********************************** ")

    try:
        year = int(input("Informe o ano à ser consultado: "))

        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            print(f"O ano {year} é bissexto!")
        else:
            print(f"O ano {year} não é bissexto!")

    except ValueError:
        print('Ano informado está inválido!')


if __name__ == "__main__":
    leap()