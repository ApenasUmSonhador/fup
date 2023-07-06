# Aluno: Arthur Vinicius Carneiro Nunes
# Matrícula: 552341

"""
Lógica:
    1. Receber INTEIRO qtde (Quantidade de alunos da turma).
        1.1. Tratar casos inválidos: qtde não inteiro ou qtde não pertencer ao intervalo (0,30].
    2. Receber matrícula de cada aluno.
        2.1. Tratar casos inválidos: matrícula não inteiro ou matrícula não pertencer ao intervalo [10^5, 10^6).
    3. Receber 3 notas de cada aluno.
        3.1 Tratar casos inválidos: nota não ser float ou nota não pertencer ao intervalo [0,10].
    4. Colocar (2) e (3) em um dicionário.
    5. Armazenar (4) em uma lista de alunos.
    6. Dessa lista de alunos:
        6.1. Achar menor AP.
        6.2. Retirar a menor AP de cada aluno.
        6.3. Realizar a média de cada aluno.
        6.4. Mostrar média de cada aluno.
            6.4.1. A ordem NÃO é baseada na matrícula, mas na ordem em que foi adicionada no programa.
    7. Saída do programa baseada em (6.4) ou nos casos inválidos (1.1, 2.1, 3.1)
"""

# Funções:
"""
Observações:
    1. Sobre os 'return "erro"':
        Sempre detecto erro via esse retorno, se ele for encontrado paro o programa imediatamente, fica macarrão mas funciona de maneira decente.
"""
# (1.1)
def trata_qtde(qtde):
    try:
        qtde = int(qtde)
        if qtde > 0 and qtde <= 30:
            return qtde
        return "erro"
    except ValueError:
        return "erro"

# (2.1)
def trata_matricula(matricula):
    try:
        matricula = int(matricula)
        if matricula >= (10**5) and matricula < (10**6):
            return matricula
        return "erro"
    except ValueError:
        return "erro"

# (3.1)
def trata_nota(nota):
    try:
        nota = float(nota)
        if nota >= 0 and nota <= 10:
            return nota
        return "erro"
    except ValueError:
        return "erro"

# (4)
def faz_dicionario(matricula,ap1,ap2,ap3):
    dicionario = {
        "matricula": matricula,
        "ap1": ap1,
        "ap2": ap2,
        "ap3": ap3,
    }
    return dicionario

# (6.1)
def acha_menor_ap(dicionario):
    menor = dicionario["ap1"]
    menor_ap = "ap1"
    if menor > dicionario["ap2"]:
        menor = dicionario["ap2"]
        menor_ap = "ap2"
    if menor > dicionario["ap3"]:
        menor = dicionario["ap3"]
        menor_ap = "ap3"
    return menor_ap

# (6.2)
def retirar_menor_ap(dicionario,tirar):
    novo_dicionario = {}
    if tirar == "ap1":
        novo_dicionario = {
        "matricula": dicionario["matricula"],
        "ap2": dicionario["ap2"],
        "ap3": dicionario["ap3"],
        }
    elif tirar == "ap2":
        novo_dicionario = {
        "matricula": dicionario["matricula"],
        "ap1": dicionario["ap1"],
        "ap3": dicionario["ap3"],
        }
    else:
        novo_dicionario = {
        "matricula": dicionario["matricula"],
        "ap1": dicionario["ap1"],
        "ap2": dicionario["ap2"],
        }
    return novo_dicionario

# (6.3)
def realiza_media(dicionario):
    media = 0
    for chave in dicionario:
        if chave != "matricula":
            media += dicionario[chave]
    media = media / 2
    return media

# Variável para conferir se há erro e parar programa imediatamente.
erro = False

# Código principal:
"""
Minha defesa a favor do código macarrão:
    É um momento de tensão fazer a prova com o tempo contando contra nós,nesse sentido fiz o código na maneira que estava mais obvia para mim.
    PS: Pelo menos a lógica ficou oh, top.
"""

# (1)
qtde = input()
qtde = trata_qtde(qtde)

# (1.1)
if qtde == "erro":
    print("invalido")


else:
    lista_de_alunos = []
    for i in range(qtde):
        # (2)
        matricula = input()
        matricula = trata_matricula(matricula)
        # (2.1)
        if matricula == "erro":
            erro = True
            break

        else:
            # (3)
            ap1 = input()
            ap1 = trata_nota(ap1)

            # (3.1)
            if ap1 == "erro":
                erro = True
                break
            else:
                # (3)
                ap2 = input()
                ap2 = trata_nota(ap2)

                # (3.1)
                if ap2 == "erro":
                    erro = True
                    break
                else:
                    # (3)
                    ap3 = input()
                    ap3 = trata_nota(ap3)

                    # (3.1)
                    if ap3 == "erro":
                        erro = True
                        break
                    else:
                        # (4)
                        aluno = faz_dicionario(matricula,ap1,ap2,ap3)
                        # (5)
                        lista_de_alunos.append(aluno)

    if erro is False:
        nova_lista_de_alunos = []
        # (6)
        for i in range(qtde):
            aluno_atual = lista_de_alunos[i]
            # (6.1)
            tirar = acha_menor_ap(aluno_atual)
            # (6.2)
            aluno_atual = retirar_menor_ap(aluno_atual,tirar)
            # (6.3)
            nova_lista_de_alunos.append(aluno_atual)

    # (7)
        for aluno in nova_lista_de_alunos:
            media = realiza_media(aluno)
            # (6.4)
            print(media)
    # (3.1)
    else:
        print("invalido")