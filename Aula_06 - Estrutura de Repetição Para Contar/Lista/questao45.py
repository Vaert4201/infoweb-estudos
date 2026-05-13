inicio = int(input("Digite o início: "))
fim = int(input("Digite o fim: "))

soma = 0
num = inicio

while num <= fim:
    if num > 1:
        i = 2

        while i * i <= num:
            if num % i == 0:
                break
            i += 1
        else:
            # só entra aqui se NÃO houve break → número é primo
            soma += num

    num += 1

print("Soma dos primos:", soma)