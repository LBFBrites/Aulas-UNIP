#um programa que inverte uma dada string

def Inverter(texto):
    resultado = ""
    for letra in texto:
        resultado = letra + resultado
    return resultado

texto = input("Insira o texto: ")
print(Inverter(texto))