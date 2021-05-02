#########################################################################
############################## JOGO DO NIM ##############################
#########################################################################

def computador_escolhe_jogada(n, m):
    if n <= m:
        return n #se for possível tirar todas as peças restantes e ganhar o jogo
    else:
        if n % (m+1) > 0: #se houver resto, ou seja, se não for múltiplo
            return n % (m+1) #retirar sempre o resto, pois sendo o resto zero, significa que o valor é múltiplo
        return m #o máximo, caso não seja possível deixar múltiplo de (m+1)

##############################
##############################
##############################

def usuario_escolhe_jogada(n, m):
    valor = input('\nQuantas peças você vai tirar? ')
    try:
        valor = int(valor)
    except:
        print('\nOops! Jogada inválida! Tente de novo.')

    while (valor > m) | (valor <= 0) | (valor > n):
        print('\nOops! Jogada inválida! Tente de novo.')
        valor = int(input('\nQuantas peças você vai tirar? '))

    return valor

##############################
##############################
##############################

def partida():

    # Fazer loop para checar n
    while True:
        n = input('Quantas peças? ')
        try:
            n = int(n)
        except:
            print('\nATENÇÃO, Escolha um número inteiro diferente de 0!\n')
            continue
        if (n > 0):
            break
        else:
            print('\nEscolha um número inteiro diferente de 0!\n')

    # Fazer loop para checar m
    while True:
        m = input('\nLimite de peças por jogada? ')
        try:
            m = int(m)
        except:
            print('\nATENÇÃO, Escolha um número inteiro diferente de 0 e menor ou igual ao número total de peças!\n')
            continue
        if (m <= n) & (m != 0):
            break
        else:
            print('\nEscolha um número inteiro diferente de 0 e menor ou igual ao número de peças!')

# Define quem começa
    jogador = 0
    valor = 0

    if (n % (m+1) == 0):
        jogador = 1 #se n for múltiplo de m+1 o jogador é o usuário
        print('\nVocê começa!')
        # manter o loop apenas enquanto n > 0
        while n > 0:
            if jogador == 1:
                valor = usuario_escolhe_jogada(n, m)
                if valor == 1:
                    print('\nVocê tirou uma peça.')
                else:
                    print('\nVocê tirou', valor, 'peças.')

                n = n - valor #atualiza o n
                if (n == 1):
                    print('\nAgora resta apenas uma peça no tabuleiro.')
                elif (n == 0):
                    None
                else:
                    print('\nAgora restam', n, 'peças no tabuleiro.')

                jogador = 2 #passa a jogada para o computador

            else:
                valor = computador_escolhe_jogada(n, m)
                if valor == 1:
                    print('\nO computador tirou uma peça.')
                else:
                    print('\nO computador tirou', valor, 'peças.')

                n = n - valor #atualiza o n novamente
                if (n == 1):
                    print('\nAgora resta apenas uma peça no tabuleiro.')
                elif (n == 0):
                    None
                else:
                    print('\nAgora restam', n, 'peças no tabuleiro.')

                jogador = 1 #passa a jogada para o usuário

        # quando acabar o loop (while) pois n == 0
        if jogador == 1: #caso n seja 0 e o computador foi o último a jogar (por isso jogador = 1)
            print('\nFim do jogo! O computador ganhou!')
            return 2 #para computar ponto ao computador
        else: #o que eu espero não acontecer, hehe
            print('\nFim do jogo! Você ganhou!')
            return 1 #para computar ponto ao usuário

    else: #(n % (m+1) != 0)
        jogador = 2 #se n não for múltiplo de m+1 o jogador é o computador
        print('\nComputador começa!')
        # manter o loop apenas enquanto n > 0
        while n > 0:
            if jogador == 2:
                valor = computador_escolhe_jogada(n, m)
                if valor == 1:
                    print('\nO computador tirou uma peça.')
                else:
                    print('\nO computador tirou', valor, 'peças.')

                n = n - valor #atualiza o n
                if (n == 1):
                    print('\nAgora resta apenas uma peça no tabuleiro.')
                elif (n == 0):
                    None
                else:
                    print('\nAgora restam', n, 'peças no tabuleiro.')

                jogador = 1 #passa a jogada para o usuário

            else:
                valor = usuario_escolhe_jogada(n, m)
                if valor == 1:
                    print('\nVocê tirou uma peça.')
                else:
                    print('\nVocê tirou', valor, 'peças.')

                n = n - valor #atualiza o n novamente
                if (n == 1):
                    print('\nAgora resta apenas uma peça no tabuleiro.')
                elif (n == 0):
                    None
                else:
                    print('\nAgora restam', n, 'peças no tabuleiro.')

                jogador = 2 #passa a jogada para o computador

        # quando acabar o loop (while) pois n == 0
        if jogador == 1: #caso n seja 0 e o computador foi o último a jogar (por isso jogador = 1)
            print('\nFim do jogo! O computador ganhou!')
            return 2 #para computar ponto ao computador
        else: #o que eu espero não acontecer, hehe
            print('\nFim do jogo! Você ganhou!')
            return 1 #para computar ponto ao usuário

##############################
##############################
##############################

def campeonato():
    numero_de_partidas = 1
    placar_usuario = placar_computador = 0

    while numero_de_partidas < 4:

        print('\n**** Rodada', numero_de_partidas, '****\n')

        if partida() == 1:
            placar_usuario += 1
        else:
            placar_computador += 1

        numero_de_partidas += 1

    print('\n**** Final do campeonato! ****')
    print('\nPlacar: Você', placar_usuario, 'X', placar_computador, 'Computador')


##############################
##############################
##############################

def main():

        print('\nBem-vindo ao jogo NIM! Escolha:\n')
        print('1 - para jogar uma partida isolada\n2 - para jogar um campeonato')
        escolha = None

        # Starting loop
        while True:
            escolha = input('\nDigite sua escolha aqui: ')

            try:
                escolha = int(escolha)
            except:
                print('\nATENÇÃO, Essa não é uma escolha válida!')
                continue

            if (escolha == 1) | (escolha == 2):
                break
            else:
                print('\nATENÇÃO, Essa não é uma escolha válida!')

        if escolha == 1:
            print('\nVocê escolheu uma partida isolada!')
            partida()
        elif escolha == 2:
            print('\nVocê escolheu um campeonato!')
            campeonato()

main()
