# Importando biblioteca para limpar().
from os import system, name

# Declarando e inicializando variáveis.
notas = []
alunos = 0
soma = 0

# Função que limpa terminal.
def limpar():
    if name == "nt":
        system("cls")

    else:
        system("clear")

# Função que lembrará ao professor a condição de saída.
def lembrar_sair():
    limpar()
    print("\n-------------- BEM VINDO AO PROGRAMA --------------")
    print('Professor, para sair do algoritmo, digite "sair".')
    print("---------------------------------------------------\n")

# Algoritmo:
while True:
    lembrar_sair()
    notas.append(input(f"Qual a nota do {alunos+1}° aluno? ").strip().lower())

    # Condição escolhida para terminar o programa.
    if notas[alunos] == "sair":
        notas.pop(alunos)
        break
    
    # Demais casos.
    try:
        # Tratando caso professor digite notas inválidas.
        if float(notas[alunos]) < 0 or float(notas[alunos]) > 10:
            limpar()
            notas.pop(alunos)
            print("\n-------------------- ERROR ----------------------")
            print(f'Professor, só serão aceitas notas entre 0 e 10.')
            print("---------------------------------------------------\n")
            
        else:
            alunos += 1

    # Tratando caso professor digite strings diferentes de "sair".
    except ValueError:
        limpar()
        notas.pop(alunos)
        print("\n-------------------- ERROR ----------------------")
        print(f'Professor, utilize apenas numerais ou digite "sair".')
        print("---------------------------------------------------\n")

    
for nota in notas:
    soma += float(nota)

if alunos > 1:
    limpar()
    print("\n---------------- MUITO OBRIGADO ------------------")
    print(f'Professor, a média da sua turma de {alunos} alunos é de {(soma/alunos):.2f}')
    print("---------------------------------------------------\n")
elif alunos == 1:
    limpar()
    print("\n---------------- MUITO OBRIGADO ------------------")
    print(f'     Professor, a nota do teu único aluno é {soma}')
    print("---------------------------------------------------\n")
else:
    limpar()
    print("\n---------------- MUITO OBRIGADO ------------------")
    print(f'Professor, p senhor não colocou nenhum aluno, sendo assim não há media')
    print("---------------------------------------------------\n")
