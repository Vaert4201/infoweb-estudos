texto = input('Digite qualquer string: ')

vogais = 0

for letra in texto:
    if letra.lower() in 'aeiou':
        vogais += 1

print(vogais)