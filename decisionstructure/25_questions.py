def questions():
    print("**********************************")
    print("         Interrogatório!          ")
    print("**********************************")

    yes = []

    call = input('a. Telefonou para a vítima? [S/N]: ')
    validate(call)
    add(call, yes)

    local = input('b. Esteve no local do crime? [S/N]: ')
    validate(local)
    add(local, yes)

    live = input('c. Mora perto da vítima [S/N]: ')
    validate(live)
    add(live, yes)

    money = input('d. Devia para a vítima? [S/N]: ')
    validate(money)
    add(money, yes)

    work = input('e. Já trabalhou com a vítima? [S/N]: ')
    validate(work)
    add(work, yes)

    total = sum(yes)
    result(total)


def validate(answer):
    if (answer[0].upper() != 'S') and (answer[0].upper() != 'N'):
        print('Resposta Incorreta!')
        exit()


def add(answer, yes):
    if answer[0].upper() == 'S':
        yes.append(1)


def result(total):
    switcher = {
        2: "Suspeita",
        3: "Cúmplice",
        4: "Cúmplice",
        5: "Assassino"
    }

    print(switcher.get(total, 'Inocente'))


if __name__ == "__main__":
    questions()
