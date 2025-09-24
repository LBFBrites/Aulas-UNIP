#Peça um numero ao usuario e verifique se é primo

def Primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

numero = int(input("Digite um numero: "))
if Primo(numero):
    print(f"O numero {numero} é primo!")
else:
    print(f"O numero {numero} não é primo")