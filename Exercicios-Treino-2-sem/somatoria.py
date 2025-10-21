#uma função que receba um numero "n" e calcule a soma de todos os numeros de 1 a n

def Calcular(n):
    soma = 0
    i = 1
    while i <= n:
        soma += i
        i += 1
    return soma

numero = int(input("Digite um numero: "))
print(Calcular(numero))