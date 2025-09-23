import hashlib
import json
import os
from datetime import datetime
from colorama import Fore, init
import pyfiglet
from rich.console import Console
from rich.table import Table

################################################################### init
init(autoreset=True);
console = Console();

############################################################################# menu's shenanigans
def ExibirTitulo(texto):
    banner = pyfiglet.figlet_format(texto, font="slant");
    print(Fore.CYAN + banner);

def MostrarMenu(opcoes):
    i = 1
    for opcao in opcoes:
        print(f"{i} - {opcao}");
        i += 1;

def LerOpcao():
    while True:
        opcao_digitada = input("Selecione uma opção: ")
        if opcao_digitada.isdigit():
            return int(opcao_digitada);
        else:
            print(Fore.RED + "! Opção inválida, digite um número.");

def LimparTela():
    os.system('cls');

################################################################################### criptografia
def CriptoSenha(senha):
    salt = "biblioteca_digital_2025";
    senha_com_salt = senha + salt;
    return hashlib.sha256(senha_com_salt.encode()).hexdigest();

def VerificarSenha(senha_digitada, hash_armazenado):
    return CriptoSenha(senha_digitada) == hash_armazenado;

############################################################################# dados
def CarregarDados(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f);
    return {};

def SalvarDados(arquivo, dados):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False);

################################################################### files & dados
usuarios_file = "usuarios.json";
livros_file = "livros.json";

usuarios = CarregarDados(usuarios_file);
livros = CarregarDados(livros_file);

################################################################### users
def CadastrarUsuario():
    username = input("Digite o username: ");
    if any(u["username"] == username for u in usuarios.values()):
        print(Fore.RED + " ! Usuário já existe!");
        return;
    
    senha = input("Digite a senha (mín. 6 caracteres): ");
    if len(senha) < 6:
        print(Fore.RED + " ! Senha muito curta!");
        return;
    
    nome = input("Nome completo: ");
    novo_id = str(len(usuarios) + 1);
    usuarios[novo_id] = {
        "username": username,
        "password_hash": CriptoSenha(senha),
        "tipo": "user",
        "nome_completo": nome,
        "data_criacao": datetime.now().strftime("%Y-%m-%d")
    }
    SalvarDados(usuarios_file, usuarios);
    print(Fore.GREEN + " Usuário cadastrado com sucesso!");

def Login():
    username = input("Usuário: ");
    senha = input("Senha: ");
    for user in usuarios.values():
        if user["username"] == username and VerificarSenha(senha, user["password_hash"]):
            print(Fore.GREEN + f" Bem-vindo, {user['nome_completo']}!");
            return user;
    print(Fore.RED + "! Usuário ou senha inválidos.");
    return None;

def ListarUsuarios():
    table = Table(title=" Usuários Cadastrados");
    table.add_column("ID", style="cyan");
    table.add_column("Username");
    table.add_column("Nome Completo");
    table.add_column("Tipo");
    table.add_column("Data Criação");

    for uid, u in usuarios.items():
        table.add_row(uid, u["username"], u["nome_completo"], u["tipo"], u["data_criacao"]);
    
    console.print(table);

################################################################### livros
def CadastrarLivro():
    isbn = input("ISBN (somente números): ");
    if not isbn.isdigit():
        print(Fore.RED + " ! ISBN deve ser numérico!");
        return;
    if isbn in livros:
        print(Fore.RED + " ! Livro já cadastrado!");
        return;
    
    titulo = input("Título: ");
    autor = input("Autor: ");
    categoria = input("Categoria: ");
    novo = {
        "titulo": titulo,
        "autor": autor,
        "categoria": categoria,
        "disponivel": True,
        "data_cadastro": datetime.now().strftime("%Y-%m-%d")
    }
    livros[isbn] = novo;
    SalvarDados(livros_file, livros);
    print(Fore.GREEN + "Livro cadastrado com sucesso!");

def ListarLivros():
    table = Table(title="Acervo - Livros Cadastrados");
    table.add_column("ISBN", style="cyan");
    table.add_column("Título");
    table.add_column("Autor");
    table.add_column("Categoria");
    table.add_column("Status");

    for isbn, l in livros.items():
        status = "Disponível" if l.get("disponivel", True) else "Emprestado"
        table.add_row(isbn, l.get("titulo","-"), l.get("autor","-"), l.get("categoria","-"), status);
    
    console.print(table);

################################################################### seleção simples
def SelecionarLivro():
    if not livros:
        print(Fore.RED + "Nenhum livro cadastrado ainda.")
        return None
    ListarLivros()
    escolhido = input("Digite o ISBN do livro que deseja selecionar: ")
    print(Fore.GREEN + f"Livro selecionado: {escolhido}")
    return escolhido

################################################################### emprestimos & devolução
def AbrirEmprestimos():
    print(Fore.YELLOW + "=== Menu de Empréstimos ===")
    SelecionarLivro()
    print(Fore.YELLOW + "Empréstimo em análise...")

def AbrirDevolucao():
    print(Fore.YELLOW + "=== Menu de Devolução ===")
    SelecionarLivro()
    print(Fore.GREEN + "Devolução concluída.")

################################################################### menu
def MenuPrincipal():
    opcoes = [
        "Login", "Cadastrar Usuário", "Listar Usuários",
        "Cadastrar Livro", "Listar Livros",
        "Empréstimos", "Devolução", "Sair"
    ];
    while True:
        ExibirTitulo("Biblioteca");
        MostrarMenu(opcoes);
        opt = LerOpcao();

        if opt == 1:
            Login();
        elif opt == 2:
            CadastrarUsuario();
        elif opt == 3:
            ListarUsuarios();
        elif opt == 4:
            CadastrarLivro();
        elif opt == 5:
            ListarLivros();
        elif opt == 6:
            AbrirEmprestimos();
        elif opt == 7:
            AbrirDevolucao();
        elif opt == 8:
            print(Fore.YELLOW + "Saindo do sistema...");
            break
        else:
            print(Fore.RED + "Opção inválida.");

############################################################### main
if __name__ == "__main__":
    LimparTela();
    MenuPrincipal();