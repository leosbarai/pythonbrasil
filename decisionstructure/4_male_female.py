def male_female():
    print("**********************************")
    print("  Sexo Masculino ou Feminino!")
    print("**********************************")

    gender = input("Informe o caracter sexo M ou F: ")

    if (gender[0].upper() == 'M'):
        print("Sexo Masculino!")
    elif (gender[0].upper() == 'F'):
        print("Sexo Feminino!")
    else:
        print("Sexo inválido!")

if __name__ == "__main__":
    male_female()