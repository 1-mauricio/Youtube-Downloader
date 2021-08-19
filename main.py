from pytube import YouTube

fim = False
while not fim:
    link = input("Digite o link do vídeo que deseja baixar: ")
    path = input("Digite o diretório que deseja salvar o vídeo: ")
    yt = YouTube(link)

    print(f"Título: {yt.title}")
    print(f"Número de views: {yt.views}")
    tempo = yt.length / 60
    if tempo > 60:
        tempo /= 60
        print(f"Duração aproximada do vídeo: {tempo:.2f} horas")
    else:
        print(f"Tamanho do vídeo: {tempo:.2f} minutos")

    aud = input("Baixar apenas áudio?(S/N) ")
    if aud == "S":
        video = yt.get_audio_only("mp4")
    else:
        res = int(input("1 - A maior possível\n2 - 720p\n3 - 480p\nEscolha a resolução do vídeo: "))
        if res == 1:
            video = yt.streams.get_highest_resolution()
        elif res == 2:
            video = yt.streams.get_by_resolution("720p")
        else:
            video = yt.streams.get_by_resolution("480p")

    print("Baixando...")
    video.download(path)
    print("Download Completo")
    loop = input("Baixar novamente?(S/N) ")
    loop = loop.upper()
    if loop == "N":
        fim = True
        print("Programa encerrado")
