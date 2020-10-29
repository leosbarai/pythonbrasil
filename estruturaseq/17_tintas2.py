from math import ceil

def tintas():
    print("**********************************")
    print("         Loja de Tintas!")
    print("**********************************")

    area = float(input("Informe a área a ser pintada em m²: "))
    litros_tinta = area / 6

    litros_tinta = round(litros_tinta * 1.1)

    lata = litros_tinta // 18

    perc_galao = round(((litros_tinta / 18) - lata) * 100)

    if perc_galao <= 60:
        galao = ceil(perc_galao / 20)
    else:
        lata += 1
        galao = 0

    total_lata = lata * 80.0
    total_galao = galao * 25.0

    if lata > 0 and galao > 0:
        print("Você vai precisar de {} lata(s) e {} galão(ões) de tinta e custará R$ {}".format(lata, galao, (total_lata + total_galao)))
    elif lata > 0 and galao == 0:
        print("Você vai precisar de {} lata(s) e custará R$ {}".format(lata, total_lata))
    elif lata == 0 and galao > 0:
        print("Você precisará de {} galão(ões) e custará R$ {}".format(galao, total_galao))

if __name__ == "__main__":
    tintas()