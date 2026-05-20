n = float(input('Digite a quantidade de notas dos alunos:'))
contador = 1
maior = float('-inf')
while contador <= n:
    nota = float(input(f'Nota do aluno {contador}:'))
    maior = max(maior, nota)
    contador += 1
print(f'Maior nota: {maior}')

