#Erro de Programação-
#idade = int(input("Digite sua idade: "))
#if idade <= 12:
   #print("Criança")
#if idade <= 17:
   #print("Adolescente")
#if idade <= 59:
   #print("Adulto")
#else:
   #print("Idoso")

idade = int(input("Digite sua idade: "))
if 0 <= idade <= 12:
   print("Criança")
elif 13 <= idade <= 17:
   print("Adolescente")
elif 18 <= idade <= 59:
   print("Adulto")
elif idade >= 60:
   print("Idoso")

