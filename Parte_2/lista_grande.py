'''
Escreva a função lista_grande(n),
que recebe como parâmetro um número inteiro n
e devolve uma lista contendo n números inteiros aleatórios.
'''

import random

def lista_grande(n): 
    list = []
    for i in range(n):
        aleatorio = random.randint(-100,100)
        list.append(aleatorio)

    return list
