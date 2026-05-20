a, b = map(int, input('Digite os dois números do MMC:') .split())
maior = max(a, b)
mmc = maior
while mmc % a != 0 or mmc % b != 0:
    mmc += maior
print(mmc)
