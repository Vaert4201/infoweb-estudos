import math

area = float(input('Digite o valor da área em metros quadrados:'))
piccolo = math.ceil(area / 1.5)
print(f'O valor da área em metros quadrados é:{area}')
print(f'A quantidade mínima de caixas de água para preencher a área é:{piccolo}')
