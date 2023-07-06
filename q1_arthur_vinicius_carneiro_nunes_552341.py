# Aluno: Arthur Vinicius Carneiro Nunes
# Matrícula: 552341

"""
Lógica:
    1. Receber INTEIROS n(linha) e m(coluna).
        1.1. Tratar casos inválidos: n e m não serem inteiros ou n,m não estarem no intervalo [1,50].
    2. Receber NATURAIS e preencher matriz nxm.
        2.1. Tratar casos inválidos: números recebidos não inteiros ou serem < 0.
    3. Achar qual o valor da maior linha.
    4. Achar qual o valor da maior coluna.
    5. Comparar valores (3) e (4) e escolher o maior.
    6. Saída de acordo com casos inválidos (1.1) e (2.1) ou do maior (5).
"""

# Funções:
"""
Observações:
    1. Sobre os 'return "erro"':
        Sempre detecto erro via esse retorno, se ele for encontrado paro o programa imediatamente, fica macarrão mas funciona de maneira decente.
    2. Sobre "Unused variables":
        Sei que é má prática utilizar for quando não aproveitamos o uso da variável, porém, utilizarei para fins de melhor compreensão.
"""

# (1.1)
def trata_nm(entrada):
    try:
        entrada = int(entrada)
        if entrada >= 1 and entrada <= 50:
            return entrada
        return "erro"
    except ValueError:
        return "erro"

# (2) e (2.1)
def preenche_matriz(linhas,colunas):
    matriz = []

    for i in range(linhas):
        linha = []
        for j in range(colunas):
            try:
                entrada = int(input())
                if entrada < 0:
                    return "erro"
                linha.append(entrada)

            except ValueError:
                return "erro"

        matriz.append(linha)
    return matriz

# (3)
def maior_linha(matriz):
    maior_linha = 0
    for i in range(len(matriz)):
        linha_atual = 0
        for j in range(len(matriz[0])):
            linha_atual += matriz[i][j]
        if linha_atual > maior_linha:
            maior_linha = linha_atual
    return maior_linha

# (4)
def maior_coluna(matriz):
    maior_coluna = 0
    for j in range(len(matriz[0])):
        coluna_atual = 0
        for i in range(len(matriz)):
            coluna_atual += matriz[i][j]
        if coluna_atual > maior_coluna:
            maior_coluna = coluna_atual
    return maior_coluna

# (5)
def compara_maior(valor_linha,valor_coluna):
    if valor_coluna >= valor_linha:
        return valor_coluna
    else:
        return valor_linha


# Código principal:
"""
Minha defesa a favor do código macarrão:
    É um momento de tensão fazer a prova com o tempo contando contra nós,nesse sentido fiz o código na maneira que estava mais obvia para mim.
    PS: Pelo menos a lógica ficou oh, top.
"""


n = input()
n = trata_nm(n)

if n == "erro":
    # (6)
    print("invalido")

else:
    # (1)
    m = input()
    # (1.1)
    m = trata_nm(m)

    if m == "erro":
        # (6)
        print("invalido")

    else:
        # (2) e (2.1)
        matriz = preenche_matriz(n,m)
        if matriz == "erro":
            # (6): (1.1) e (2.1)
            print("invalido")

        else:
            # (3)
            maior_linha = maior_linha(matriz)
            # (4)
            maior_coluna = maior_coluna(matriz)
            # (5)
            maior = compara_maior(maior_linha,maior_coluna)
            # (6): (5)
            print(maior)