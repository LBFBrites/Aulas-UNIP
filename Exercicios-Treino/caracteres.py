#um programa que conta os caracteres da mensagem

def Contar(frase):
    letras = digitos = espacos = 0
    for ch in frase:
        if ch.isalpha():
            letras += 1
        elif ch.isdigit():
            digitos += 1
        elif ch.isspace():
            espacos += 1
    return letras, digitos, espacos

frase = input("Digite a frase: ")
letras, digitos, espacos = Contar(frase)
print("Digitos: ", digitos, "| Letras: ", letras, "| Espacos: ", espacos)