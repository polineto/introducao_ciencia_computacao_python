numero = input('Digite um número inteiro: ')

if (int(numero) % 3 == 0) & (int(numero) % 5 == 0):
    print('FizzBuzz')
else:
    print(numero)
