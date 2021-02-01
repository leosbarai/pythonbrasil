def grades():
    print("********************************** ")
    print("             Notas! ")
    print("********************************** ")

    try:
        grade_one = float(input("Informe a 1ª nota: "))
        grade_two = float(input("Informe a 2ª nota: "))
        avg = round((grade_one + grade_two)/2, 2)

        if 0 <= avg <= 4.0:
            concept = "E"
            situation = "Reprovado"
        elif 4.0 < avg <= 6.0:
            concept = "D"
            situation = "Reprovado"
        elif 6.0 < avg <= 7.5:
            concept = "C"
            situation = "Aprovado"
        elif 7.5 < avg >= 9.0:
            concept = "B"
            situation = "Aprovado"
        elif 9.0 < avg >= 10.0:
            concept = "A"
            situation = "Aprovado"

        if avg >= 0 and avg <= 10:
            print(f'A média das notas {grade_one} e {grade_two} é {avg}. Com o conceito {concept} você está {situation}!')
        else:
            print('A nota informada está incorreta!')

    except ValueError:
        print('A nota informada está incorreta!')


if __name__ == "__main__":
    grades()