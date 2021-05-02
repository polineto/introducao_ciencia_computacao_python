numero1 = float(input('Digite o primeiro número inteiro: '))
numero2 = float(input('Digite o segundo número inteiro: '))
numero3 = float(input('Digite o terceiro número inteiro: '))
numero4 = float(input('Digite o quarto número inteiro: '))

import math

distancia = math.sqrt( ((numero1 - numero3) ** 2) + ( (numero2 - numero4) ** 2 ))

if distancia >= 10:
    print('longe')
else:
    print('perto')
