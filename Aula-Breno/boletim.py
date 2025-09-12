import pyfiglet
from colorama import init, Fore, Back, Style
from rich.console import Console
from rich.table import Table
import os

init()
alunos = []
disciplinas = []
notas = []

def LimparTela():
    os.system('cls')

LimparTela()
init(autoreset=True)
console = Console()

print(Fore.CYAN + pyfiglet.figlet_format("Escola Novo Saber"))
print(Fore.GREEN + pyfiglet.figlet_format("Sistema de lançamento da minha caceta alada flamejante"))
Style.RESET_ALL

# Mostrar título
def titulo():
    banner = pyfiglet.figlet_format("Novo Saber")
    print(Fore.CYAN + banner)
    print(Fore.YELLOW + "Sistema Escolar de Lançamento de Notas\n" + Style.RESET_ALL)

# Cadastro fixo de 3 alunos
alunos = []
for i in range(3):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    turma = input("Digite a turma: ")
    alunos.append({"id": i+1, "nome": nome, "turma": turma})

# Cadastro fixo de 2 disciplinas
disciplinas = []
for i in range(2):
    codigo = input(f"Digite o código da disciplina {i+1}: ").upper()
    nome = input("Digite o nome da disciplina: ")
    disciplinas.append({"codigo": codigo, "nome": nome})

# Lançamento de notas
notas = {}
for aluno in alunos:
    for disc in disciplinas:
        print(f"\nLançando notas para {aluno['nome']} em {disc['nome']}:")
        p1 = float(input("Nota P1: "))
        p2 = float(input("Nota P2: "))
        trab = float(input("Nota Trabalho: "))
        notas[(aluno["id"], disc["codigo"])] = {"P1": p1, "P2": p2, "Trabalho": trab}

# Gerar boletim por aluno
for aluno in alunos:
    table = Table(title=f"Boletim - {aluno['nome']} ({aluno['turma']})")
    table.add_column("Disciplina")
    table.add_column("P1")
    table.add_column("P2")
    table.add_column("Trabalho")
    table.add_column("Média")
    table.add_column("Status")

    for disc in disciplinas:
        n = notas[(aluno["id"], disc["codigo"])]
        media = (n["P1"] + n["P2"] + n["Trabalho"]) / 3
        if media >= 7:
            status = Fore.GREEN + "Aprovado"
            Style.RESET_ALL
        elif media >= 5:
            status = Fore.YELLOW + "Recuperação"
            Style.RESET_ALL
        else:
            status = Fore.RED + "Reprovado"
            Style.RESET_ALL
        table.add_row(disc["nome"], str(n["P1"]), str(n["P2"]), str(n["Trabalho"]), f"{media:.1f}", status)

    console.print(table)
    print("\n")


