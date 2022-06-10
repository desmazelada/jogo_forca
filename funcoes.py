import os


def limpaTela():
    os.system("cls")


def convertCaps(texto):
    return texto.upper()


def reiniciaVariaveis():
    global i
    global chances
    global temDicas
    global letrasReveladas
    i = 0
    chances = 5
    temDicas = bool
    letrasReveladas = 0


def defineJogadores():
    limpaTela()
    print("\n******Jogo da Forca******\n")

    global desafiante
    global competidor
    desafiante = convertCaps(input("Digite o nome do Desafiante: "))
    competidor = convertCaps(input("Digite o nome do Competidor: "))
    limpaTela()


def definePalavra():
    print(f'Essa tela deve ser visualizada apenas por {desafiante}.')
    global palavraChave
    palavraChave = convertCaps(
        input(f'\nInsira aqui a palavra que vai enforcar {competidor}: '))
    global letrasPalavra
    global palavraOculta
    letrasPalavra = list(palavraChave)
    palavraOculta = list("*" * (len(palavraChave)))


def defineDicas():
    print(
        f'\nDisponibilize três palavras como dicas para ajudar {competidor} se ele(a) precisar pedir ajuda aos universitários. Seja criativo!\n')
    global dicas
    dicas = []
    while len(dicas) < 3:
        dica = convertCaps(input("Insira aqui uma dica: "))
        dicas.append(dica)
    limpaTela()
    print(f'Seja bem-vindo(a) ao jogo, {competidor}...\n\n')
    return dicas


def contaErro():
    global chances
    global ganhou
    chances = chances - 1
    if chances > 0:
        print(f'Cuidado, {competidor}. Só te restam {chances} chances!\n')


def testaLetra():
    global letra
    global ganhou
    global letrasReveladas
    letra = convertCaps(input("\nInsira aqui o seu chute: "))
    limpaTela()

    try:
        letra in letrasPalavra
        letrasReveladas = letrasReveladas + letrasPalavra.count(letra)
        localLetra = letrasPalavra.index(letra)

        if letra in letrasPalavra:
            print(f'Ótimo chute, {competidor}!\n')

        for localLetra, value in enumerate(letrasPalavra):
            if value == letra:
                palavraOculta[localLetra] = letra
    except:
        print("Sinto muito, você errou...")
        contaErro()
    finally:
        global vencedor
        global perdedor
        if letrasReveladas == len(letrasPalavra):
            ganhou = True
            vencedor = f'Competidor {competidor}'
            perdedor = f'Desafiante {desafiante}'
            atualizaHistorico()
            mostraVencedor()
        elif chances == 0:
            ganhou = False
            vencedor = f'Desafiante {desafiante}'
            perdedor = f'Competidor {competidor}'
            atualizaHistorico()
            mostraVencedor()
        else:
            mostraPalavra()


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
        print("Suas dicas acabaram! Tá díficil? Que pena!\nDe qualquer jeito você vai ter que arriscar uma letra.\n")
        mostraPalavra()


def mostraPalavra():
    global temDicas
    global palavraOculta
    print(f'Sua palavra é:\n\n{"".join(palavraOculta)}\n')

    if temDicas:
        escolha = input(
            "Deseja arriscar uma letra?\n(0) Jogar\n(1) Pedir dica\n\n")

        if escolha == "0":
            testaLetra()
        elif escolha == "1":
            mostraDica()

        else:
            limpaTela()
            print("Escolha uma opção válida!")
            mostraPalavra()
    else:
        testaLetra()


def atualizaHistorico():
    global historico
    historico = open('historico.txt', 'a', encoding="utf8")
    historico.writelines(
        f'Palavra: {palavraChave} // Vencedor: {vencedor} // Perdedor: {perdedor}\n')
    historico.close()


def mostraVencedor():
    if ganhou:
        print(
            f'Você venceu o jogo e se livrou da forca. Parabéns, {competidor}!\n')
        print("  ┌─┐  ─┐ ")
        print("  │▒│ /▒/")
        print("  │▒│/▒/")
        print("  │▒│/▒/")
        print("  │▒ /▒/─┬─┐")
        print("  │▒│▒|▒│▒│")
        print(" ┌┴─┴─┐-┘─┘")
        print(" │▒┌──┘▒▒▒│")
        print(" └┐▒▒▒▒▒▒┌┘")
        print("  └┐▒▒▒▒┌\n")
        print(f'A palavra era {palavraChave}.\n{desafiante} perdeu o jogo!\n')
    else:
        print(
            f'Oh não!!!! Você gastou todas as suas chances e acabou sendo enforcado! Que pena, {competidor}...\n')
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /|\ ")
        print("|    | ")
        print("|   / \ ")
        print("_      \n")
        print(f'A palavra era {palavraChave}.\n{desafiante} venceu o jogo!\n')

    historico = open('historico.txt', 'r', encoding="utf8")
    dados = historico.read()
    print('Histórico do Jogo:')
    print(f'\n{dados}\n')


def apagaHistorico():
    historico = open('historico.txt', 'w')
    historico.writelines('')
    historico.close()
