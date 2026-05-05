#Erro de Programação-
#n = int(input('Entrada: '))
#if n % 3 == 0:
   #print(f'{n} é múltiplo de 3')
#elif n % 5 == 0:
#    print(f'{n} é múltiplo de 5')
# elif n % 3 == 0 and n % 5 == 0:
#    print(f'{n} é múltiplo de 3 e de 5')
# else:
#    print(f'{n} não é múltiplo nem de 3 nem de 5')


n = int(input('Entrada: '))
if n % 3 == 0:
   print(f'{n} é múltiplo de 3')
elif n % 5 == 0:
   print(f'{n} é múltiplo de 5')
elif n % 15 == 0:
   print(f'{n} é múltiplo de 3 e de 5')
else:
   print(f'{n} não é múltiplo nem de 3 nem de 5')

   #O erro estava no segundo elif, pois se um número for multiplo de 3 e 5 ao mesmo tempo, não será necessariamente múltiplo dos dois, ele terá que ser de um número que na vdd
   # assim será multiplo dos dois, como 15, que é o menor deles.

