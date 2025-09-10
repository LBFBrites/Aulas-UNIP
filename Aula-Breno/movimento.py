pos_ini = float(input("Digite a posição inicial: "))
pos_fin = float(input("Digite a posição final: "))
V = float(input("Digite o valor de velocidade em km/h: "))

dist = (pos_fin - pos_ini)
tempo_horas = dist / V
horas = int(tempo_horas)
minutos = int((tempo_horas - horas) * 60)

print(f"O tempo necessário para percorrer o trajeto é de {horas} horas e {minutos} minutos.")
