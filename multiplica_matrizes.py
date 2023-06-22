def preenche_matrizes(a,b,nome):
    matriz = []
    for i in range(a):
        linha = []
        for j in range(b):
            linha.append(int(input(f"Digite o número que ocupa a posição [{i},{j}] na matriz {nome}.")))

        matriz.append(linha)

    return matriz

def multiplica_matrizes(a,b):
    C = []
    for i in range(len(A)):
        linha = []
        for j in range(len(B)):
            termo = 0
            for k in range(len(B[i])):
                termo += A[i][k] * B[k][j]
            linha.append(termo)
        C.append(linha)
    return C

def erro():
    print("erro")

a_l = int(input("digite o numero de linhas de A"))
a_c = int(input("digite o numero de colunas de A"))
b_l = int(input("digite o numero de linhas de B"))
b_c = int(input("digite o numero de colunas de B"))

if a_l == b_c:
    A = preenche_matrizes(a_l,a_c,"A")
    B = preenche_matrizes(b_l,b_c,"B")
    AxB = multiplica_matrizes(A,B)
    print(AxB)
else:
    erro()
