from colorama import init, Fore, Back, Style
import pyfiglet
import os
init()

def LimparTela():
    os.system('cls')

def ler_atividades():
    atividades = []

    print("=== CADASTRO DE ATIVIDADES ===")
    print("Digite 'S' em qualquer campo para sair\n")

    while True:
        print(f"--- Atividade {len(atividades) + 1} ---")
        data = input("Data (dd/mm/aaaa): ").strip()
        if data.upper() == 'S':
            break
        atividade = input("Atividade: ").strip()
        if atividade.upper() == 'S':
            break
        horas = input("Total de horas: ").strip()
        if horas.upper() == 'S':
            break
        item = {
            'data': data,
            'atividade': atividade,
            'horas': horas
        }

        atividades.append(item)
        print("Atividade cadastrada com sucesso!\n")

    return atividades


LimparTela()
print(Fore.GREEN + pyfiglet.figlet_format("A.P.S"))

titulo = "FICHA DE ATIVIDADES PRÃTICAS SUPERVISIONADAS"
print(Fore.LIGHTBLUE_EX + titulo)

# Style.RESET_ALL: Reseta todos os estilos e cores ao padrÃ£o, prevenindo que eles sejam aplicados a textos que vocÃª nÃ£o deseja estilizar.
print(Style.RESET_ALL + 'Este Ã© o texto padrÃ£o')


dados_aluno = {"nome": input("Digite seu nome: "),
               "ra": input("Digite seu RA: "),
               "curso": input("Digite seu curso: "),
               "campus": input("Digite seu Campus: "),
               "semestre": input("Digite seu Semestre: "),
               "turno": input("Digite seu Turno: ")
               }
LimparTela()
lista_atividades = ler_atividades()
print("\n=== ATIVIDADES CADASTRADAS ===")
for i, item in enumerate(lista_atividades, 1):
    print(f"Atividade {i}:")
    print(f"  Data: {item['data']}")
    print(f"  Atividade: {item['atividade']}")
    print(f"  Total de horas: {item['horas']}")
    print()
print(dados_aluno)