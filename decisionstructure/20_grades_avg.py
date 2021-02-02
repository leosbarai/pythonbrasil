def grades_avg():
    print("********************************** ")
    print("          Média das Notas! ")
    print("********************************** ")

    try:
        grade_one = float(input("Informe a 1ª nota: "))
        grade_two = float(input("Informe a 2ª nota: "))
        grade_three = float(input("Informe a 3ª nota: "))
        avg = round((grade_one + grade_two + grade_three) / 3, 2)

        if avg == 10:
            print(f'Aprovado com Distinção com a média {avg}')
        elif 7 <= avg < 10:
            print(f'Aprovado com a média {avg}')
        elif 0 <= avg < 7:
            print(f'Reprovado com a média {avg}')
        else:
            print('A nota informada está incorreta!')

    except ValueError:
        print('Valor informado está incorreto!')


if __name__ == "__main__":
    grades_avg()