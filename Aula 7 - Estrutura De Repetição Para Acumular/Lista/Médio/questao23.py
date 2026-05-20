x = float(input('Digite o seu número: '))
h = 0
n = 0

while h <= x:
    n += 1
    h += 1 / n

print(f'Maior denominador: {x}')
print(f'Valor da série harmônica: {h}')
print(f'Quantidade de termos: {n}')  #<-- O que a questão pede!!