import matriz

def soma_matrizes(A, B):
    n_lin = len(A)
    n_col = len(A[0])
    C = matriz.cria_matriz(n_lin, n_col, 0)

    for lin in range(n_lin):
        for col in range(n_col):
            C[lin][col] = A[lin][col] + B[lin][col]
    return C

if __name__ == '__main__':  # se estiver sendo executado como script

    A = [[1,2,3], [4,5,6], [7,8,9]]
    B = [[10,20,30], [40,50,60], [70,80,90]]

    print(soma_matrizes(A,B))
