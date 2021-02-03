import math

def withdraw():
    print("********************************** ")
    print("             Saque! ")
    print("********************************** ")

    try:
        amount = int(input('Informe o valor do saque: '))
        hundred_banknote = []
        fifty_banknote = []
        ten_banknote = []
        five_banknote = []
        one_banknote = []

        if 10 <= amount <= 600:
            if amount >= 100:
                amount = hundred(amount, hundred_banknote)
                print(f'{hundred_banknote[0]} nota(s) de R$ 100')

            if amount >= 50:
                amount = fifty(amount, fifty_banknote)
                print(f'{fifty_banknote[0]} nota(s) de R$ 50')

            if amount >= 10:
                amount = ten(amount, ten_banknote)
                print(f'{ten_banknote[0]} nota(s) de R$ 10')

            if amount >= 5:
                amount = five(amount, five_banknote)
                print(f'{five_banknote[0]} nota(s) de R$ 5')

            if amount >= 1:
                one(amount, one_banknote)
                print(f'{one_banknote[0]} nota(s) de R$ 1')

        else:
            print('Saque permitido apenas para valor entre R$ 10 a R$ 600.')

    except ValueError:
        print('Digite apenas números inteiros entre 10 e 600!')


def hundred(amount, hundred_banknote):
    hundred_banknote.append(math.trunc(amount / 100))
    return amount % 100


def fifty(amount, fifty_banknote):
    fifty_banknote.append(math.trunc(amount / 50))
    return amount % 50


def ten(amount, ten_banknote):
    ten_banknote.append(math.trunc(amount / 10))
    return amount % 10


def five(amount, five_banknote):
    five_banknote.append(math.trunc(amount / 5))
    return amount % 5


def one(amount, one_banknote):
    one_banknote.append(amount)


if __name__ == "__main__":
    withdraw()