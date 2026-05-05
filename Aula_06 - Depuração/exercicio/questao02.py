#Erro de Execução-
#dividendo = int(input('Digite o dividendo: '))
#divisor = int(input('Digite o divisor: '))
#quociente = dividendo / divisor
#print(f'Quociente: {quociente}')

a = int(input('Digite o dividendo:'))
b = int(input('Digite o divisor:'))
if b != 0:
    q = a / b
    print(f'Quociente: {q}')
else:
    print('O valor não está definido.')

    # o erro foi por conta que como a divisão por 0 nois não sabemos ao certo oq é, o programa n consegue realizar ela com clareza, por isso sempre q for executar uma conta de divisão por 0 no seu programa, defina quanto será o valor por 0.
