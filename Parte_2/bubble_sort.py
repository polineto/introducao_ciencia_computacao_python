def bubble_sort(lista):
    '''o bubble coloca sempre o maior número no final de cada rodada,
    por isso eu vou definir a ultima posição a testar'''
    ate_onde_ir = len(lista) - 1
    for i in range(ate_onde_ir, 0, -1):
        for j in range(i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                print(lista)

    return lista
    
