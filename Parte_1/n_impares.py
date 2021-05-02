number = int(input('Digite o valor de n: '))

inicio = 1
while number > 0:
    if (inicio % 2) != 0:
        print(inicio)
        inicio += 2
    number -= 1
