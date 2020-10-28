def gerarPlaylistMusica():
    musicaPlaylist = []

    while True:
        musica = input("Digite o nome da música. [0] para sair: ")

        if musica == "0":
            break
        elif musica not in musica:
            musicaPlaylist.append(musica)
        else:
            print("Música não cadastrada no sistema!")
    
    if len(musicaPlaylist) != 0:
        print(f"Playlist criada: {musicaPlaylist}")
    else:
        print("Nenhuma música cadastrada na playlist")

