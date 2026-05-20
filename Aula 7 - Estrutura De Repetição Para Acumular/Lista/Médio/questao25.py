l = int(input())
a = 1
n = 1

while a <= l:
    n += 1
    a = a + 2 * n - 1

print(f'n={n}')
print(f'a({n})={a}')