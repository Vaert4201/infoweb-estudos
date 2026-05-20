n = int(input('Digite a sua tabuada: '))
i = 0
while i <= 9 and n > 0:
    i += 1
    resultado = n * i
    print(f'{n} x {i} = {resultado}')

