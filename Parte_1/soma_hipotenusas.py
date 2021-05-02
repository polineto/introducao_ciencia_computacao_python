def é_hipotenusa(n):

    hipo = []

    for h in range(1, (n + 1), 1):

        for ca in range(1, (h + 1), 1):

            for co in range(1, (h + 1), 1):

                if (h ** 2) == (ca ** 2) + (co ** 2):

                    hipo.append(h)

    return hipo


def soma_hipotenusas(n):
    
    soma = sum(set(é_hipotenusa(n)))

    return soma
    
