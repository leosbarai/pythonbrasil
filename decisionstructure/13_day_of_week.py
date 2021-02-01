def return_day():
    print("********************************** ")
    print("          Dia da Semana! ")
    print("********************************** ")

    try:
        day = int(input("Informe o número correspondente ao dia da semana: "))
        day_of_week(day)

    except ValueError:
        print('Por favor, informar um número inteiro!')

def day_of_week(day):
    switcher = {
        1: "Domingo",
        2: "Segunda-feira",
        3: "Terça-feira",
        4: "Quarta-feira",
        5: "Quinta-feira",
        6: "Sexta-feira",
        7: "Sábado"
    }

    print(switcher.get(day, 'Dia da semana inválido'))


if __name__ == "__main__":
    return_day()