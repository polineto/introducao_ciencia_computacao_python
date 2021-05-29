def menor_nome(nomes):

    lista_nomes = []
    for nome in nomes:
        lista_nomes.append(nome.lower().strip())

    lista_n_char = []
    for i in range(len(lista_nomes)):
        lista_n_char.append(len(lista_nomes[i]))

    ind = lista_n_char.index(min(lista_n_char)) #index do menor valor

    return lista_nomes[ind].capitalize()
        
