#elabore uma função para contar o numero de vogais em uma dada palavra

def ContadorVogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0
    for letra in texto:
        if  letra in vogais:
            contador += 1
    return contador


texto = input("insira uma palavra: ")
print("O numero de vogais na palavra é de: ", ContadorVogais(texto))