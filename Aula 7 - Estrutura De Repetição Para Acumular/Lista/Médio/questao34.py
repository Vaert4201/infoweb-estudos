b, e, m = map(int, input('Digite respectivamente a base, o expoente e o módulo desejados: ') .split())

resultado = 1

while e > 0:

    if e % 2 == 1:
        resultado = (resultado * b) % m

    b = (b * b) % m
    e //= 2

print(resultado)