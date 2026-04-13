import math

num = float(input('Digite o valor da raiz:'))
raiz = math.sqrt(num)
bulma = math.ceil(raiz)
chichi = math.floor(raiz)
print(f'O valor exato da raiz quadrada é:{raiz}')
print(f'O valor arredondado para cima da raiz quadrada é:{bulma}')
print(f'O valor arredondado para baixo da raiz quadrada é:{chichi}')
