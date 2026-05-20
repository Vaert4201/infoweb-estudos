num1, num2, num3 = map(int, input('Digite três números inteiros:') .split())
if num1 <= num2 and num1 <= num3:
    menor = num1
    if num2 <= num3:
        meio = num2
        maior = num3
    else:
        meio = num3
        maior = num2
elif num2 <= num1 and num2 <= num3:
    menor = num2
    if num1 <= num3:
        meio = num1
        maior = num3
    else:
        meio = num3
        maior = num1
else:
    menor = num3
    if num2 <= num1:
        meio = num2
        maior = num1
print(menor, meio, maior)
