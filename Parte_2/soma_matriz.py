def soma_matrizes(m1, m2):
    if dimensoes(m1) == dimensoes(m2):
        matriz = []
        for i in range(len(m1)):
            linha = []
            for j in range(len(m1[0])):
                valor = (m1[i][j] + m2[i][j])
                linha.append(valor)
            matriz.append(linha)

        return matriz
        
    else:
        return False
    

def dimensoes(matriz):
    m = len(matriz)
    n = len(matriz[0])
    return (str(m) + 'X' + str(n))
