def preenche_matriz(l,c):
    matriz = []
    for i in range(l):
        linha = []
        for j in range(c):
            linha.append(input())
        matriz.append(linha)
    return matriz

def sub_matriz(m1,m2):
    matriz = []
    for i in range(len(m1)):
        linha = []
        for j in range(len(m1[i])):
            
            linha.append(m1[i][j] - m1[i][j])
        matriz.append(linha)
    return matriz

def sum_matriz(m1,m2):
    matriz = []
    for i in range(len(m1)):
        linha = []
        for j in range(len(m1[i])):
            
            linha.append(m1[i][j] + m1[i][j])
        matriz.append(linha)
    return matriz

def mult_matrizes(m1,m2):
    if len(m1[0]) != len(m2):
        return "erro"

    matriz = []
    for i in range(len(m1)):
        linha = []
        for j in range(len(m2)):
            termo = 0
            for k in range(len(m2[i])):
                termo += m1[i][k] * m2[k][j]
            linha.append(termo)
        matriz.append(linha)
    return matriz

def transpor_matriz(m):
    matriz = []
    for i in range(len(m[0])):
        linha = []
        for j in range(len(m)):
            linha.append(m[j][i])
        matriz.append(linha)
    return matriz

def confere_simetria(m):
    if m == transporta_matriz(m):
        return True
    return False
