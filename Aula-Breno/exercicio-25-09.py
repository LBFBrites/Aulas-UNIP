def Calcular(k, q1, q2, p1, p2):
    d = (((p2[0] - p1[0]) ** 2) + ((p2[1] - p1[1]) ** 2)) ** 0.5
    resultado = (k * q1 * q2) / d ** 2
    return resultado

k = 5
q1 = 6
q2 = 4
p1 = (5,1)
p2 = (5,10)
print(Calcular(k, q1, q2, p1, p2))