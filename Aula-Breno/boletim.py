import pyfiglet
from colorama import init, Fore, Back, Style
import rich
import os

init()
alunos = []
disciplinas = []
notas = []

def LimparTela():
    os.system('cls')

LimparTela()
print(Fore.CYAN + pyfiglet.figlet_format("Escola Novo Saber"))
print(Fore.GREEN + pyfiglet.figlet_format("Sistema de lançamento da minha piroca alada flamejante"))


titulo = "Boletim estudantil"
print(Fore.LIGHTBLUE_EX + titulo)

# Style.RESET_ALL: Reseta todos os estilos e cores ao padrÃ£o, prevenindo que eles sejam aplicados a textos que vocÃª nÃ£o deseja estilizar.
print(Style.RESET_ALL + 'nada mais para ver aqui')

def cadastro_aluno():
    id_aluno = len(alunos) + 1
    nome = input("Nome do aluno: ")
    turma = input("Turma: ")
    alunos.append({"id": id_aluno, "nome": nome, "turma": turma})
    print(Fore.YELLOW + f"Aluno {nome} cadastrado com sucesso!\n")

def cadastro_disciplina():
    codigo = input("Código da disciplina: ")
    nome = input("Nome da disciplina: ")
    disciplinas.append({"codigo": codigo, "nome": nome})

def lancar_notas():
    if not alunos or not disciplinas:
        print(Fore.RED + "Cadastre ao menos uma nota e uma disciplina\n")
        return

print("Alunos disponiveis")
for aluno in alunos:
    print(f"{aluno['id']} - {aluno['nome']} ({aluno['turma']})")
id_aluno = int(input("Digite o ID do aluno: "))

print("Disciplinas disponíveis:")
for disc in disciplinas:
    print(f"{disc['codigo']} - {disc['nome']}")
codigo = input("Digite o código da disciplina: ").upper()


