n = int(input("Quantos números você vai digitar? "))

peq = 0
med = 0
gra = 0

contador = 1

while contador <= n:
    num = float(input(f"Número {contador}: "))

    if num < 10:
        peq += 1
    elif 10 <= num <= 100:
        med += 1
    else:
        gra += 1

    contador += 1

print(f'Pequenos: {peq}')
print(f'Médios: {med}')
print(f'Grandes: {gra}')
