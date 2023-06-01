# Importando biblioteca para limpar().
from os import system, name

# Variável que decidirá inicio (True) e fim (False) do algoritmo.
algoritmo = True

# String armazenando meses do ano, adicionei espaços para que cada "mês" tivesse 9 caracteres.
meses = "  JaneiroFevereiro    Março    Abril     Maio    Junho    Julho   Agosto Setembro  Outubro Novembro Dezembro"

# Função que limpa terminal.
def limpar():
    if name == "nt":
        system("cls")

    else:
        system("clear")

# Loop para caso o usuário queira executar novamente.
while algoritmo:
    limpar()
    # Recebendo do usuário Data no formato dd/mm/aaaa.
    data = input("Digite sua data de nascimento no formato dd/mm/aaaa: ")
    if data[6:].isdigit() and data[0:2].isdigit() and len(data[6:]) == 4:
        # Descobrindo mês por extenso do usuário:
        try:
            mes_int = int(data[3:5])
            # Tratando meses inválidos.
            if mes_int > 12 or mes_int < 1:
                print("\n-------------------- ERROR ----------------------")
                print("Por favor, digite apenas meses de 01 a 12.")
                print("---------------------------------------------------\n")

            else:
                mes_txt = meses[((mes_int - 1)*9):((mes_int)*9)]
                # Saída.
                print(f"Você nasceu em {data[0:2]} de {mes_txt.lstrip()} de {data[6:11]}.")

        except ValueError:
            print("\n-------------------- ERROR ----------------------")
            print("Por favor, digite apenas datas no formato dd/mm/aaaa.")
            print("---------------------------------------------------\n")
    # Tratando formatos inváidos.
    else:
        print("\n-------------------- ERROR ----------------------")
        print("Por favor, digite apenas datas no formato dd/mm/aaaa.")
        print("---------------------------------------------------\n")

    algoritmo = (input("Deseja executar novamente? \n[S] [N]").title().strip()).startswith("S")
