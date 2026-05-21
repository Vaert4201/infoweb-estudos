a = int(input())
b = int(input())

for i in range(max(a, b)):

    if b == 0:

        break

    r = a % b
    a = b
    b = r                      #Principio do MDC - Divide os dois que dará esse resultado!

print(a)