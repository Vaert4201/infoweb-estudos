from tabulate import tabulate

tabela = []

for c in range(0, 101, 10):

    f = c * 9.5 + 32
    k = c + 273.15

    if c < 15:
        
        clas = 'fria'

    elif 15 <= c <= 25:

        clas = 'agradável'

    else:

        clas = 'quente'

    tabela.append([c, f, k, clas])

print(tabulate(tabela, headers=['Celsius', 'Fahrenheit', 'Kelvin', 'Classificação' ], tablefmt = 'grid'))