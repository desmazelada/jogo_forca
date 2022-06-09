import os


def limpaTela():
    os.system("cls")


def convertCaps(texto):
    return texto.upper()


def definePalavra(texto):
    global palavraChave
    palavraChave = convertCaps(input(texto))
    global letrasPalavra
    letrasPalavra = list(palavraChave)


def defineDicas(texto):
    print(texto)
    dicas = []
    while len(dicas) < 3:
        dica = input("Insira aqui uma dica: ")
        dicas.append(dica)
    return dicas
