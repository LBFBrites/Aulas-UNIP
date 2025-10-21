#elabore um programa que exiba a tabuada de um dado numero por input usando while

def Tabuada():
    numero = int(input("Insira o numero desejado: "))
    contagem = 0
    while (contagem <= 10):
        print(numero * contagem)
        contagem += 1

Tabuada()