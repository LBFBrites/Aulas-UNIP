import pyfiglet
import os
from colorama import Fore, Style, init
import hashlib
import hashlib
import json
from datetime import datetime

def criptografar_senha(senha):
    salt = "biblioteca_digital_2025"  # Salt fixo para simplicidade
    senha_com_salt = senha + salt
    hash_senha = hashlib.sha256(senha_com_salt.encode()).hexdigest()
    return hash_senha

def verificar_senha(senha_digitada, hash_armazenado):
    hash_digitada = criptografar_senha(senha_digitada)
    return hash_digitada == hash_armazenado

# Exemplo de estrutura do usuarios.json
usuarios = {
    "1": {
        "username": "admin",
        "password_hash": "null",
        "tipo": "admin",
        "nome_completo": "Administrador Sistema",
        "data_criacao": "2025-09-16"
    },
    "2": {
        "username": "joao123",
        "password_hash": "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f",
        "tipo": "user",
        "nome_completo": "João Silva Santos",
        "data_criacao": "2025-09-16"
    }
}
hash_atual = usuarios["1"]["password_hash"];
print(f"O hash atual do usuário 1 é: {hash_atual}");

senha = input("Digite a senha: ");
hash_novo = criptografar_senha(senha);

usuarios["1"]["password_hash"] = hash_novo;
print(f"O hash da senha do usuário 1 é: {usuarios["1"]["password_hash"]}")