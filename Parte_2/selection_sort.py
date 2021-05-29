def ordena(lista):

    for i in range(len(lista) - 1):
        posicao_do_menor = i # assumo inicialmente que o menor número está na primeira posição

        for j in range( (i + 1), len(lista) ):
            if lista[j] < lista[posicao_do_menor]:
                posicao_do_menor = j

        lista[i], lista[posicao_do_menor] = lista[posicao_do_menor], lista[i]

    return lista
