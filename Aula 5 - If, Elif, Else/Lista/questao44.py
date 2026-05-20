l1, l2, l3 = map(float, input('Digite o valor dos três lados do triângulo:') .split())
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    if l1 == l2 == l3:
        print('Equilátero.')
    elif l1 != l2 and l2 != l3:
        print('Escaleno.')
    else:
        print('Isosceles.')
else:
    print('Não forma um triângulo.')
