matriz = []
def constroi_matriz(n_linhas,n_colunas):
    matriz = []
    for i in range(int(n_linhas)):
        linha = []
        for j in range(int(n_colunas)):
            linha.append(input(f"Digite o elemento que está na posição [{i},{j}] da matriz."))
        matriz.append(linha)
    return matriz

l = input("digite o  numero de linhas")
c = input("digite o numeor de colunas")

constroi_matriz(l,c)
print(matriz)