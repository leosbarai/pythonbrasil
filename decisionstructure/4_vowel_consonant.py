def vowel_consonant():
    print("********************************** ")
    print(" Verifica se é vogal ou consoante! ")
    print("********************************** ")

    letter = input("Informe uma letra: ")
    vowels = ['A', 'E', 'I', 'O', 'U']

    if letter[0].isalpha():
        if letter[0].upper() in vowels:
            print(f"{letter[0]} é uma vogal")
        else:
            print(f"{letter[0]} é uma consoante!")
    else:
        print(f"O caractere {letter[0]} não é uma letra!")


if __name__ == "__main__":
    vowel_consonant()