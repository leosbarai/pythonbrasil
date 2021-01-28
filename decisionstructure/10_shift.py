def shift():
    print("********************************** ")
    print("            Turno! ")
    print("********************************** ")

    shift = input('Informe o turno em que estuda (M-matutino, V-Vespertino ou N-Noturno): ')

    if (shift[0].upper() == 'M'):
        print("Bom dia!")
    elif (shift[0].upper() == 'V'):
        print("Boa tarde!")
    elif (shift[0].upper() == 'N'):
        print("Boa noite!")
    else:
        print("Valor inválido!")


if __name__ == "__main__":
    shift()