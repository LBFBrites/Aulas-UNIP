import math

x_lancador = float(input("Digite a posição inicial x do lançador: "))
y_lancador = float(input("Digite a posição inicial y do lançador: "))
x_alvo = float(input("Digite a posição x do alvo: "))
y_alvo = float(input("Digite a posição y do alvo: "))
t = float(input("Digite o tempo para atingir o alvo: "))

g = 9.8

if(y_lancador < y_alvo): g = -9.8
else: g= 9.8
 
#calculando as diferenças de posição de x e y : alvo - lançador (final - inicial)
dx = x_alvo - x_lancador 
dy = y_alvo - y_lancador

#calculo usando s = s0+v0t + a/2 * t²
vx = dx / t
vy = (dy + 0.5 * g * t**2) / t
# v0 = raíz de (vx²) + (vy²)
v0 = float(math.sqrt(vx**2 + vy**2))

print(f"A velocidade inicial em X necessária para atingir o alvo é de:  {vx:.2f} m/s")
print(f"A velocidade inicial em Y necessária para atingir o alvo é de:  {vy:.2f} m/s")
print(f"A velocidade inicial necessária para atingir o alvo é de:  {v0:.2f} m/s")