numeros = input("Digite 3 números separados por espaço: ").split()

numeros = [int(n) for n in numeros]

numeros.sort()

print(numeros)



