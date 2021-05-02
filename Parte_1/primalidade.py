num = int(input('Digite um número inteiro: '))

div = 0
cont = 0

if (num == 0) | (num == 1):
    print('não primo')
else:
    while (div < num) & (cont < 3):
        div += 1
        if (num % div) == 0:
            cont += 1
    if cont == 2:
        print('primo')
    else:
        print('não primo')
