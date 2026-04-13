import math

tempo = float(input('Digite a quantidade de horas passadas:'))
horas = math.floor(tempo)
minutos = math.floor((tempo - horas) * 60)
print(f'Tempo: {horas} hora(s) e {minutos} minuto(s)')
