import os
import time

i = 0
chances = 5
temDicas = bool


def limpaTela():
    os.system("cls")


def convertCaps(texto):
    return texto.upper()


def defineJogadores():
    limpaTela()
    print("\n******Jogo da Forca******\n")

    global desafiante
    global competidor
    desafiante = input("Digite o nome do Desafiante: ")
    competidor = input("Digite o nome do Competidor: ")
    limpaTela()


def definePalavra():
    print(f'Essa tela deve ser visualizada apenas por {desafiante}.')
    global palavraChave
    palavraChave = convertCaps(
        input(f'\nInsira aqui a palavra que vai enforcar {competidor}: '))
    global letrasPalavra
    letrasPalavra = list(palavraChave)


def defineDicas():
    print(
        f'\nDisponibilize três palavras como dicas para ajudar {competidor} se ele(a) precisar pedir ajuda aos universitários. Seja criativo!\n')
    global dicas
    dicas = []
    while len(dicas) < 3:
        dica = input("Insira aqui uma dica: ")
        dicas.append(dica)
    print(f'Seja bem-vindo(a) ao jogo, {competidor}...\n')
    limpaTela()
    return dicas


def contaErro():
    global chances
    chances = chances - 1
    if chances > 0:
        print(f'Cuidado, {competidor}, só te restam {chances} chances!\n')
        mostraPalavra()


def testaLetra():
    global letra
    letra = convertCaps(input("Insira aqui o seu chute: "))
    limpaTela()

    try:
        if letra in letrasPalavra:
            print("Ótimo chute!")
    except:
        print("Que pena, você errou...")
        contaErro()


def mostraDica():
    limpaTela()

    global i
    global temDicas
    if i <= 2:
        temDicas = True
        print(f'A dica para adivinhar a palavra é: {dicas[i]}\n\n')
        i = i + 1
        mostraPalavra()
    else:
        temDicas = False
        print("Suas dicas acabaram! Agora você precisa arriscar uma letra.\n")
        mostraPalavra()

def mostraLetra():
    global letra
    global palavraOculta
    palavraOculta = list("*" * (len(palavraChave)))
    for i in range(len(letrasPalavra)):
	    if letra == letrasPalavra[i]:
		    palavraOculta[i] = letra

def mostraPalavra():
    global temDicas
    mostraLetra()
    print(f'Sua palavra é:\n\n{"".join(palavraOculta)}\n')

    if temDicas:
        escolha = input(
            "Deseja arriscar uma letra?\n(0) Jogar\n(1) Pedir dica\n")

        if escolha == "0":
            testaLetra()
        elif escolha == "1":
            mostraDica()

        else:
            print("Escolha uma opção válida!")
            mostraPalavra()
    else:
        testaLetra()

def finalJogo():
    letrasReveladas = int
    if chances == 0:
        print('Oh não!!!! Você gastou todas as suas chances e acabou sendo enforcado!')
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /|\ ")
        print("|    | ")
        print("|   / \ ")
        print("_      ")
        print()
        palavraCerta = print('A palavra era', palavraChave)
        vencedor = print('Vencedor:', desafiante)
        competidor = print('Perdedor: ', competidor)
    elif letrasReveladas == len(letrasPalavra):
        print('Você venceu o jogo e se livrou da forca. Parabéns!')
        palavraCerta = print('A palavra era', palavraChave)
        vencedor = print('Vencedor:', desafiante)
        competidor = print('Perdedor: ', competidor)

        
        

    


