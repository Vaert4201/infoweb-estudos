base = int(input('Digite o valor da sua base:'))
exp = int(input('Digite o valor do seu expoente:'))
resultado = 1
x = 0
while x < exp:
    resultado *= base
    x += 1
print(resultado)