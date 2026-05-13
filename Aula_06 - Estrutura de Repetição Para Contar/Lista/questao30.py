n = int(input('Digite um número inteiro:'))
if n <= 1:
    print('Não é primo')
else:
    x = 2

while x * x <= n:
    if n % x == 0:
        print('Não é primo')
        break

    else:
        print('É primo')
    x += 1

#comando break é utilizado para sair do laço de repetição, ou seja, quando o número for divisível por algum número entre 2 e a raiz quadrada de n, ele não é primo e o programa para de verificar os próximos números. Se o laço terminar sem entrar no if, significa que o número é primo e o programa imprime "É primo".