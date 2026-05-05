n = int(input('Digite qualquer número inteiro positivo:'))
x = 1
while x <= n:
    if x % 3 == 0 and x % 12 != 0:
        print('Fizz')
    elif x % 4 == 0 and x % 12 != 0:
        print('Buzz')
    elif x % 12 == 0:
        print('FizzBuzz')
    else:
        print(x)
    x += 1