def soma_lista(lista):
    if len(lista) == 1:
        return lista[0]
    elif len(lista) == 0:
        return False
    return lista[0] + soma_lista(lista[1:])
