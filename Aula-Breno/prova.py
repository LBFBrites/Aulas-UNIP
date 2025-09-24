def criptografar(mensagem, chave):
    resultado = ""
    for letra in mensagem:
        valor = ord(letra)
        valor += chave
        resultado += chr(valor)
    return resultado

criptografia = criptografar("cripto", 5)
print(criptografia)
        