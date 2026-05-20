n = int(input('Digite qualquer número: '))
div = 1
x = 0

while div < n:

    if n % div == 0:
        x += div

    div += 1
    
if n == x:
    print('É perfeito.')
else:
    print('Não é perfeito.')
   
