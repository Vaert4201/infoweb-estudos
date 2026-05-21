n = int(input())

peq = 0
med = 0
gra = 0

print()

for i in range(1, n):

    num = int(input())

    if num < 10:

        peq += 1
    
    elif 10 <= num <= 100:

        med += 1

    else:

        gra += 1

print(f'Pequenos: {peq}')
print(f'Médios: {med}')
print(f'Grandes: {gra}')

