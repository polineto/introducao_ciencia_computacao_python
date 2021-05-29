def conta_letras(frase, contar = 'vogais'):

    n_vogais = 0
    n_consoantes = 0

    palavras = []
    for palavra in frase.split():
        palavras.append(palavra)

    for i in range(len(palavras)):
        for letra in palavras[i]:
            if letra in ['a', 'e', 'i', 'o', 'u']:
                n_vogais += 1
            else:
                n_consoantes += 1

    if contar ==  'vogais':
        return n_vogais
    else:
        return n_consoantes
