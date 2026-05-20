a, b = map(int, input('Digite os dois números do MDC:') .split())
while b != 0:
    a, b = b, a % b
print(a)


