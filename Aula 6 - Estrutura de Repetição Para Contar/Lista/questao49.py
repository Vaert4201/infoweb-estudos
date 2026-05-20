n = int(input('Digite a quantidade de números inteiros que você deseja:'))
soma = 0
media = 0
maior = float('-inf')
menor = float('inf')
contador = 1
num = []
while contador <= n:
    x = float(input(f'Número {contador}: '))
    num.append(x)
    soma += x
    maior = max(maior, x)
    menor = min(menor, x)
    contador += 1

media = soma / n

acima_media = 0
i = 0

while i < n:
    if num[i] > media:
        acima_media += 1
    i += 1


print(f'Soma: {soma}')
print(f'Média: {media}')
print(f'Maior valor: {maior}')
print(f'Menor valor: {menor}')
print(f'Valores acima da média: {acima_media}')
