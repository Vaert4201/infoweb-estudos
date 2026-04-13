import math

cat1 = float(input('Digite o valor do cateto a:'))
cat2 = float(input('Digite o valor do cateto b:'))
hip = math.sqrt(cat1**2 + cat2**2)
print(f'O valor da hipotenusa é:{hip}')