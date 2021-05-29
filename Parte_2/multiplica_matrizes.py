import matriz

def mat_mul(A, B):

    n_linA, n_colA = len(A), len(A[0])
    n_linB, n_colB = len(B), len(B[0])
    assert n_colA == n_linB

    C = [] 

    for i in range(n_linA):
        C.append([])
        for j in range(n_colB):
            C[i].append(0)
            for k in range(n_colA):
                C[i][j] += A[i][k] * B[k][j]

    return C


if __name__ == '__main__':
    A = [[1,2,3], [4,5,6]]
    B = [[1,2], [3,4], [5,6]]
    print(mat_mul(A,B))
    
