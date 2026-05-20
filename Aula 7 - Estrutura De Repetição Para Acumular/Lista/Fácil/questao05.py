n = int(input('Digite a sua quantidade de notas: '))
x = 0
notas = []
while x < n:
    nota = float(input(f'Nota {x + 1}: '))
    notas.append(nota)
    x += 1
media = sum(notas) / x
print(media)

