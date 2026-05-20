n = int(input())

div = 1
qtd = 0

while div <= n:

    if n % div == 0:
        qtd += 1
    
    div += 1

print(qtd)