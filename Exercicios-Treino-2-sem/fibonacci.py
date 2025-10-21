#uma função que leia o numero e faça o fibonacci

def Fibo(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Digite o numero desejado: "))
Fibo(n)