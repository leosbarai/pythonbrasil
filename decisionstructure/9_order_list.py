def order():
    print("********************************** ")
    print("         Ordenação! ")
    print("********************************** ")

    list = []
    list.append(float(input('Informe a 1ª número: ')))
    list.append(float(input('Informe a 2ª número: ')))
    list.append(float(input('Informe a 3ª número: ')))

    sorted_list = sorted(list, reverse=True)

    print(f'Ordenação decrescente da lista: {sorted_list}')


if __name__ == "__main__":
    order()