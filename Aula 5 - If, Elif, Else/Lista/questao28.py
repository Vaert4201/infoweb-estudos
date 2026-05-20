num1, num2 = map(int, input('Digite dois números inteiros:') .split())
if sum([num1, num2]) > 100:
    print('Soma grande.')
else:
    print('Soma pequena.')