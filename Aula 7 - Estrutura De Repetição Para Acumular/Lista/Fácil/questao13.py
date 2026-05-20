n = int(input('Digite o seu número: '))
contagem = 0
while n > 0:
    n //= 10
    contagem += 1
print(contagem)