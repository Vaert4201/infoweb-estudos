n = int(input('Digite a quantidade de notas dos alunos:'))
contador = 1
menor = float('inf')
while contador <= n:
    nota = float(input(f'Nota do aluno {contador}:'))
    menor = min(menor, nota)
    contador += 1
print(f'Menor nota: {menor}')

# -inf --> infinito negativo e se utiliza com o max para encontrar o maior valor
# inf --> infinito positivo e se utliza com o min para encontrar o menor valor
