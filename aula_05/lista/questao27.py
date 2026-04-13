ano = int(input('Digite o seu ano de nascimento:'))
if (2026 - ano) >= 65:
    print('Elegível para aposentadoria.')
else:
    print('Não elegível para aposentadoria.')