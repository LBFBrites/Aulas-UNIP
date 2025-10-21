#o mesmo problema da prova, dessa vez pra exercitar

def Criptografar(mensagem, chave):
    resultado = ""
    for letra in mensagem:
        valor = ord(letra)
        valor += chave
        resultado += chr(valor)
    return resultado

mensagem = input("Escreva a mensagem: ")
chave = int(input("Defina o valor da chave: "))
print(Criptografar(mensagem, chave))