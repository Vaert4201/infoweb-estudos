
qtd_aprovado = 0
qtd_reprovado = 0
qtd_recuperação = 0

for i in range(10):

    nota = float(input())

    if 7 <= nota <= 10:

        qtd_aprovado += 1

    elif nota < 5:

        qtd_reprovado += 1

    elif 5 <= nota < 7:

        qtd_recuperação += 1

    else:

        print()

        print('Nota inválida! Tente um número entre 1 e 10 para equivaler corretamente a nota do aluno..')
        break


print()

print(f'Aprovados: {qtd_aprovado}')
print(f'Reprovados: {qtd_reprovado}')
print(f'Recuperação: {qtd_recuperação}')