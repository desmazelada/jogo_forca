from funcoes import limpaTela, definePalavra, defineDicas

# nome dos jogadores
limpaTela()
print("\n******Jogo da Forca******\n")
desafiante = input("Digite o nome do Desafiante: ")
competidor = input("Digite o nome do Competidor: ")
limpaTela()

# tela do desafiante
print(f'Essa tela deve ser visualizada apenas por {desafiante}.')
definePalavra(f'\nInsira aqui a palavra que vai enforcar {competidor}: ')
defineDicas(
    f'\nDisponibilize três palavras como dicas para ajudar {competidor} se ele(a) precisar pedir ajuda aos universitários. Seja criativo!\n')
limpaTela()

# tela do competidor
print(f'Seja bem-vindo(a) ao jogo, {competidor}...\n')
