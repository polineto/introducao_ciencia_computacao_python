number = int(input('Digite o valor de n: '))

fatorial = 1

if number == 0:
    print(1)
else:
    while number > 0:
        fatorial = fatorial * number
        number -= 1
    print(fatorial)
