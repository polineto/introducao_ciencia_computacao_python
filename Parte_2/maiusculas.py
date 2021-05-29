def maiusculas(frase):
    letrasMa = ''
    for caracter in frase:
        if ord(caracter) in range(65, 91, 1): #https://pt.wikipedia.org/wiki/ASCII
            letrasMa = letrasMa + caracter
    return letrasMa
