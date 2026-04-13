

letra = input('Digite qualquer letra ou número:')
if letra in 'aeiou':
    print('Uma vogal minuscula.')
elif letra.isalpha() and letra.islower():
    print('Uma consoante minuscula.')
elif letra.isdigit():
    print('Um digito.')
else:
    print('Caractere inválido.')