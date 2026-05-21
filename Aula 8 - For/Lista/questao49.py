n = int(input())

soma = 0
media = 0
maior = float('-inf')
menor = float('inf')
acima_media = 0
valores = []

print()

for i in range(1, n + 1):

    num = int(input())

    valores.append(num)

    soma += num
    maior = max(maior, num)
    menor = min(menor, num)

media = soma / n

for num in valores:

    if num > media:

        acima_media += 1

print()

print(f'Soma dos valores: {soma}')
print(f'Média dos valores: {media}')
print(f'Maior valor: {maior}')
print(f'Menor valor: {menor}')
print(f'Valores acima da média: {acima_media}')

    