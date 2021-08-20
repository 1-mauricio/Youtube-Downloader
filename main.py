from pytube import YouTube
import time


fim = False

try:
    link = input("Digite o link do vídeo que deseja baixar: ")
    path = input("Digite o diretório que deseja salvar o vídeo: ")
    yt = YouTube(link)

    while not fim:
        print(f"\nTítulo: {yt.title}")
        print(f"Número de views: {yt.views}")
        tempo = yt.length / 60
        hora = 0
        if tempo > 60:
            while tempo > 60:
                hora += 1
                tempo -=60
            print(f"Duração aproximada do vídeo: {hora:.0f} horas e {tempo:.0f} minutos")
        else:
            print(f"Tamanho aproximada do vídeo: {tempo:.2f} minutos")

        end = False
        while not end:
            print("\n--------------------------------")
            print("--------------MENU--------------")
            print("1 - A maior resolução possível")
            print("2 - 720p")
            print("3 - 480p")
            print("4 - Apenas áudio")
            print("--------------------------------")
            res = int(input(": "))
            if res == 1:
                video = yt.streams.get_highest_resolution()
                end = True
            elif res == 2:
                video = yt.streams.get_by_resolution("720p")
                end = True
            elif res == 3:
                video = yt.streams.get_by_resolution("480p")
                end = True
            elif res == 4:
                video = yt.get_audio_only("mp4")
                end = True
            else:
                print("Digite uma opção válida")


        print("Baixando...")
        video.download(path)
        print("Download Completo")
        loop = input("Baixar novamente?(S/N) ")
        loop = loop.upper()

        while loop != "S" and loop != "N":
            loop = input("Resposta incorreta. Baixar novamente?(S/N) ")
            loop = loop.upper()
        if loop == "N":
            fim = True
            print("Programa encerrado")
            time.sleep(1)
        else:
            diret = input("Utilizar o mesmo diretório? (S/N) ")
            if diret == "S":
                link = input("Digite o link do vídeo que deseja baixar: ")
                yt = YouTube(link)
            else:
                link = input("Digite o link do vídeo que deseja baixar: ")
                path = input("Digite o diretório que deseja salvar o vídeo: ")
                yt = YouTube(link)

except FileNotFoundError:
    print("O programa não conseguiu encontrar o caminho. Tente novamente")