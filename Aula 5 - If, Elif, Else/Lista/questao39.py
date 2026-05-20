sal = float(input('Digite o valor do salario do funcionario:')) 
if (sal <= 1500):
    print(sal * 0.15)
elif 1500 < sal <= 3000:
    print(sal * 0.10)
elif 3000 < sal <= 6000:
    print(sal * 0.07)
elif sal > 6000:
    print(sal * 0.03)