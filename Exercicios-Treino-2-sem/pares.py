#um programa que imprima somente os numeros pares

def Pares(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i, end=" ")

n = int(input("Digite o numero: "))
Pares(n)