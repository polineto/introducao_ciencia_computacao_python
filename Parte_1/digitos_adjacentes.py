number = int(input('Digite um número inteiro: '))

rest = number % 10
new = number // 10
adj_igual = False

while (adj_igual == False) & (new > 0):
    temp = new % 10
    if rest == temp:
        adj_igual = True
    else:
        rest = temp
        new //= 10

if adj_igual == False:
    print('não')
else:
    print('sim')
