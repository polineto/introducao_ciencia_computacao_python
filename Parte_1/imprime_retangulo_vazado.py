largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))

linhas = range(1, (altura + 1))

for linha in linhas:
    if linha == 1 or linha == altura:
        print('#' * largura)
    else:
        print('#' + (largura-2)*' ' + '#', end='')
        print()
