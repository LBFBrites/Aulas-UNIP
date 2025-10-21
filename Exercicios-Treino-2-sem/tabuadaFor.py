#mesmo da outra tabuada mas dessa vez com for

def Tabuada(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n * i}\n")

numero = int(input("digite o numero: "))
Tabuada(numero)