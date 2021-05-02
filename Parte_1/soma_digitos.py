number = int(input('Digite um número inteiro: '))

soma = 0

while (number > 0):
    soma += (number % 10)
    number //= 10

print(soma)
