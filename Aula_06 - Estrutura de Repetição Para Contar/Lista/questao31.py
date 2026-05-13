contador = 1
soma_aprov = 0
soma_reprov = 0
soma_rec = 0
soma = 0
while contador <= 10:
    n = float(input(f'Nota do aluno {contador}: '))

    if n > 10 or n < 0:
        print('Número inválido. Digite novamente.')
        continue  # volta pro inicio do loop sem incrementar o contador

    soma += n
    
    if 7 <= n <= 10:
        soma_aprov += 1
    elif n < 5:
        soma_reprov += 1
    elif 5 <= n < 7:
        soma_rec += 1
        
    contador += 1

media = soma / contador
print(f'Média da turma: {media:.2f}')
print(f'Quantidade de alunos aprovados: {soma_aprov}')
print(f'Quantidade de alunos reprovados: {soma_reprov}')
print(f'Quantidade de alunos em recuperação: {soma_rec}')

        
    