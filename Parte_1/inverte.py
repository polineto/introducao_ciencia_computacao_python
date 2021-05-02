lista = []
seguir = True

while seguir:

    n = int(input('Digite um número: '))

    if n != 0:
        lista.append(n)

    else:
        seguir = False

for i in range(len(lista), 0, -1):
    print(lista[i-1], sep = '\n')
