def selection_sort(lista):
    
    ate_onde_ir = len(lista) - 1

    for i in range(ate_onde_ir, 0, -1):

        posicao_do_maior = 0

        for j in range(i):

            if lista[j+1] > lista[posicao_do_maior]:
                posicao_do_maior = j+1

        lista[i], lista[posicao_do_maior] = lista[posicao_do_maior], lista[i]

    return lista
    
