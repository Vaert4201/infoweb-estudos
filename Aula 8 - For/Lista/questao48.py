n = int(input())

inverso = ''

for digito in str(n):

    inverso = digito + inverso

if str(n) == inverso:

    print(f'{n} é um palíndromo!')
    
else:

    print(f'{n} não é palíndromo!')