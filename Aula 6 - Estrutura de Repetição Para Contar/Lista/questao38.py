n = int(input('Digite a quantidade de números que você deseja digitar:'))
contador = 1
maior = float('-inf')
menor = float('inf')

while contador <= n:
    n = int(input(f'Número {contador}: '))
    maior = max(maior, n)
    menor = min(menor, n)
    contador += 1
print(f'Maior nota: {maior}')
print(f'Menor nota: {menor}')

