# PA = N*(a1 + aN) / 2
# r --> razão da PA, diferença entre os termos

a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
s_max = int(input('Digite a soma máxima da PA: '))

termo = a1
soma = 0
n = 0

while soma <= s_max and n < 1000:

    soma += termo
    n += 1
    termo += r

print(n)
print(soma)