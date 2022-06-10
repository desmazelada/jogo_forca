from funcoes import limpaTela, defineJogadores, definePalavra, defineDicas, mostraPalavra, reiniciaVariaveis, mostraVencedor, apagaHistorico

loop = True

while loop:
    reiniciaVariaveis()
    defineJogadores()
    definePalavra()
    defineDicas()
    mostraPalavra()
    menuFinal = True

    while menuFinal:
        final = input("Escolha uma opção:\n(0) Jogar novamente\n(1) Sair\n\n")
        if final == "0":
            menuFinal = False
            loop = True
        elif final == "1":
            apagaHistorico()
            menuFinal = False
            loop = False
        else:
            limpaTela()
            mostraVencedor()
            print("Escolha uma opção válida!")
