numero1 = input('Digite o primeiro número inteiro: ')
numero2 = input('Digite o segundo número inteiro: ')
numero3 = input('Digite o terceiro número inteiro: ')

if (int(numero1) < int(numero2)) &  (int(numero2) < int(numero3)):
    print('crescente')
else:
    print('não está em ordem crescente')
