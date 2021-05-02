# simples, é preciso corrigir para a inserção de 0 e 1.

def maior_primo(k):

    value = k
    primo = éPrimo(value)

    if éPrimo(value) == True:
        return value
    else:
        while éPrimo(value) != True:
            value -= 1
            if éPrimo(value):
                return value


def éPrimo(x):

    if x == 0:
        return False

    if x == 1:
        return False

    div = 0
    cont = 0

    while (div < x) & (cont < 3):
        div += 1
        if (x % div) == 0:
            cont += 1
    if cont == 2:
        return True
    else:
        return False
