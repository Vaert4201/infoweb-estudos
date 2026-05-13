n = int(input('Digite quantos terá a sua sequencia:'))
a = 0
b = 1
contador = 1
while contador <= n:
    print(a)
    proximo = a + b
    a = b
    b = proximo
    contador += 1
    