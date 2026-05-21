from math import prod

n = int(input())

for i in range(1, 11):

    res = prod([n, i])
    print(f'{n} x {i} = {res}')