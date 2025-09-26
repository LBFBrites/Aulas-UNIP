#recebe um numero e calcula o fatorial dele

def Fatorial(numero):
    resultado = 1
    while numero > 0:
        resultado *= numero
        numero -= 1
    return resultado

numero = int(input("Insira o numero: "))
print(Fatorial(numero))