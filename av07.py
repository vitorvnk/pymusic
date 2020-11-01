# José Vitor de Araujo - RA 603317
# Leonardo Taroco Santana - RA 607762
# Miguel Vieira Colombo - RA 602515
# Vítor Alexandre Oliveira da Silva - RA 609137
# Vitor Ferreira Rafael - RA 602711
# Rodrigo de Oliveira dos Santos - RA 60253

pymusic = {}
musicas = []


def menu() -> None:
    print("[1] - Cadastro de cantor(a)")
    print("[2] - Cadastro de música")
    print("[3] - Playlist")
    print("[4] - Sair")


def getCantorByName(name: str) -> bool:
    if pymusic[name]:
        return True
        
    return False


def getCantorById(id: str) -> bool:
    if id in list(pymusic.values()):
        return True

    return False


def getMusicaByName(musicas:list, name: str) -> bool:
    for i in musicas:
        if i['title'] == name:
            return True

    return False


def menuCantor() -> None:
    opts = {
        '1': cadastroCantor,
        '2': listagemCantores,
        '3': consultaCantor,
    }

    while True:
        print("[1] - Cadastro")
        print("[2] - Listagem de cantores")
        print("[3] - Consultar um cantor(a)")
        print("[4] - Voltar ao menu")

        opt = input("Digite uma opção:\n >> ")

        if opt == '4':
            break

        else:
            opts[opt]()    


def menuMusica() -> None:
    opts = {
        '1': cadastroMusica,
        '2': '',
        '3': '',
    }

    while True:
        print("[1] - Cadastro de música")
        print("[2] - Lista de músicas")
        print("[3] - Consultar uma música")
        print("[4] - Voltar ao menu")

        opt = input("Digite uma opção:\n >> ")

        if opt == '4':
            break

        else:
            opts[opt](musicas) 


def menuPlaylist() -> None:
    opts = {
        '1': gerarPlaylistMusica,
        '2': gerarPlaylistArtista,
        '3': menu,
    }

    print("[1] - Criar playList pelas músicas")
    print("[2] - Criar playlist pelo artista")
    print("[3] - Voltar ao menu")


def gerarPlaylistArtista():
    artistaPlaylist = []

    while True:
        artista = input("Digite o nome do artista. [0] para sair: ")

        if artista == "0":
            break
        
        elif artista not in pymusic[artista]:
            artistaPlaylist.append(artista)

        else:
            print("Artista não cadastrado no sistema!")
    
    if len(artistaPlaylist) != 0:
        print(f"Playlist criada: {artistaPlaylist}")

    else:
        print("Nenhum artista cadastrado na playlist")

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


def cadastroCantor():
    cod = int(input('Digite o código do cantor: '))
    nomecantor = input('Digite o nome do cantor: ').upper()

    if cod not in pymusic.values():
        if nomecantor not in pymusic:
            pymusic[nomecantor] = cod

        else:
            print('Nome do cantor já cadastrado!')

    else:
        print('Código já cadastrado!')
    

def cadastroMusica(musicas: list) -> None:
    titulo = input("Digite o título da música:\n >> ")

    if getMusicaByName(musicas, titulo):
        print("Música já cadastrada! Tente outra")
        return

    cod = int(input('Digite o código do cantor:\n >> '))
    
    if not getCantorById(cod):
        print("Cantor não cadastrado!")
        return

    style = input("Digite o estilo da música:\n >> ")

    musicas.append({
        'titulo': titulo,
        'cantor': cod,
        'estilo': style
    })


def consultaCantor():
    consult = input('Digite o nome do cantor para ser buscado: ').upper()
    if getCantorByName(consult) == True:
        print('Código do cantor: ', pymusic[consult])

    else:
        print('Cantor não cadastrado!')


def listagemCantores():
    print("\nLista de artistas:")
    print()
    
    for i in pymusic:
        print(f"{i} - {pymusic[i]}")


if __name__ == "__main__":
    menufuns = {
        "1": menuCantor,
        "2": menuMusica,
        "3": menuPlaylist,
    }

    while True:
        menu()
        opt = input("Digite uma opção:\n >> ")

        if opt == '4':
            break
        else:
            menufuns[opt]()


