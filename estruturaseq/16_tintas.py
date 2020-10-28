from math import ceil

def tintas():
    print("**********************************")
    print("         Loja de Tintas!")
    print("**********************************")

    area = float(input("Informe a área a ser pintada em m²: "))
    litros_tinta = area / 3
    latas = ceil(litros_tinta / 18)
    total = latas * 80.0

    print("Você precisará de {} lata(s) de tinta no valor de R$ {}.".format(latas, total))

if __name__ == "__main__":
    tintas()