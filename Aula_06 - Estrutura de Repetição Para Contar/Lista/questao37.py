n = int(input('Digite um número inteiro:'))

n = abs(n) #garante que o número também funcione para números negativos

contador = 0

while n > 0:
    n //= 10
    contador += 1
print(f'Quantidade de dígitos: {contador}')
