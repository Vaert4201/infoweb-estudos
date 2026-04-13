energia = float(input('Digite o consumo de energia usado no mês:'))
if 0 <= energia <= 100:
    print((energia * 0.40))
elif 100 < energia <= 200:
    print((energia * 0.50))
elif 200 < energia <= 300:
    print((energia * 0.65))
elif energia > 300:
    print((energia * 0.85))
