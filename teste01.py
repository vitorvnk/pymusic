def gerarPlaylistArtista():
    artistaPlaylist = []

    while True:
        artista = input("Digite o nome do artista. [0] para sair: ")

        if artista == "0":
            break
        else:
            if artista not in pymusic[name]:
                artistaPlaylist.append(artista)
            else:
                print("Artista não cadastrado no sistema!")
    
    if len(artistaPlaylist) != 0:
        print(f"Playlist criada: {artistaPlaylist}")
    else:
        print("Nenhum artista cadastrado na playlist")
