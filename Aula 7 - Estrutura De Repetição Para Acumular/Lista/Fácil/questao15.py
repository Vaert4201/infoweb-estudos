n = int(input('Digite o número: '))
k = int(input('Digite o múltiplo: '))
x = 1
while x <= n:
    if x % k == 0:
        print(x)
    x += 1