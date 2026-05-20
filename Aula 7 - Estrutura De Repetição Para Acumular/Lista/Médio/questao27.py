n = int(input('Digite o seu número: '))
x = 2
soma = 0

while x <= n:
    div = 1
    qtd = 0

    while div <= x:
        if x % div == 0:
            qtd += 1
        
        div += 1

    if qtd == 2:
        soma += x
    
    x += 1

print(soma)
