def grades():
    print("********************************** ")
    print("         Avaliação! ")
    print("********************************** ")

    try:
        grade_one = float(input("Informe a 1ª Nota: "))
        grade_two = float(input("Informe a 2ª Nota: "))
        avg = float((grade_one + grade_two) / 2)

        if avg == 10:
            print("Aprovado com Distinção!")
        elif avg >= 7:
            print("Aprovado!")
        else:
            print("Reprovado!")

    except ValueError:
        print("O valor informado não é um número!")


if __name__ == "__main__":
    grades()