def cria_matriz(n_lin, n_col, valor):
     matriz = []

     for i in range(n_lin):
          linha = []
          for j in range(n_col):
               linha.append(valor)
          matriz.append(linha)

     return matriz
