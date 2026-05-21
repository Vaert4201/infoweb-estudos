n = int(input())

primo = True

if n < 2:

    primo = False

print()

for div in range(2, n):

    if n % div == 0:
        
        primo = False

if primo:

    print(f'{n} é primo!')

else:

    print(f'{n} não é primo!')