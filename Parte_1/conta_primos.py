def n_primos(n):

    count = 0
    div = 0
    primos = 0
    numbers = range(2, (n + 1), 1) #intervalo de todos os números a serem testados

    for num in numbers: #testa todos os números no intervalo

        while num > div:
            div += 1
            if num % div == 0:
                count += 1

        if count == 2:      #se o número for primo
            primos += 1 #computo o número na contagem

        count = 0 #zero a contagem para o próximo loop
        div = 0

    return primos
