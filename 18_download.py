
def download():
    print("**********************************")
    print("      Download em minutos!")
    print("**********************************")

    tamanho_arquivo = int(input("Digite o tamanho do arquivo em MB: "))
    velocidade_internet = int(input("Informe a velocidade de sua internet em Mbps: "))
    tempo = tamanho_arquivo / velocidade_internet
    minutos = round(tempo // 60)
    segundos = round(60 * ((tempo / 60) - minutos))

    print("Seu download irá demorar aproximadamente {}m {}s.".format(minutos, segundos))

if __name__ == "__main__":
    download()