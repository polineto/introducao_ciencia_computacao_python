def ordenada(lista):
    n1 = 0
    n2 = 0
    
    for i in range(len(lista) - 1):
        if lista[i] >= lista[i+1]:
            n1 += 1
        if lista[i] <= lista[i+1]:
            n2 += 1

    if n1 == (len(lista)-1) or n2 == (len(lista)-1):
        return True
    else:
        return False


