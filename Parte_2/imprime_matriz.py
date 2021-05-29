def imprime_matriz(matriz):
    
    for lin in range(len(matriz)):
        for col in range(len(matriz[0])):
            if col == range(len(matriz[0]))[-1]:
                print(matriz[lin][col], end = "")
            else: print(matriz[lin][col], end = " ")

        print()
