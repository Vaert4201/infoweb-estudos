x = 1
prod = 1
while x <= 8:
    if x % 2 != 0:
        prod *= x
    x += 1
print(f'Produto dos impares; {prod}')