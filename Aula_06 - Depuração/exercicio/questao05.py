#Erro de programação-
#turno = int(input('Entrada: '))
#if turno == 'V' and turno == 'v':
   #print('Vespertino')
#elif turno == 'M' and turno == 'm':
   #print('Matutino')
#else:
   #print('Valor inválido')

turno = input('Entrada: ')
if turno == 'V' and turno == 'v':
   print('Vespertino')
elif turno == 'M' and turno == 'm':
   print('Matutino')
else:
   print('Valor inválido')

   #O erro estaria no uso do int, pois ele só funciona com números, que no caso da questão, seria letras ao invés de números.