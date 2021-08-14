from pytube import YouTube

link = input("Digite o link do vídeo que deseja baixar: ")
path = input("Digite o diretório que deseja salvar o vídeo: ")
yt = YouTube(link)

print("Título: ", yt.title)
print("Número de views: ", yt.views)
print("Tamanho do vídeo: ", yt.length, "segundos")

ys = yt.streams.get_highest_resolution()

print("Baixando...")
ys.download(path)
print("Download Completo")

