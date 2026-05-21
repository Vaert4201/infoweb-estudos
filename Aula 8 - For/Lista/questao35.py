n = int(input())

a = 0
b = 1

print()

for i in range(n):

    print(a, end=' ')

    proximo = a + b
    b = a
    a = proximo
