# Programowanie I R
# Zadanie fibsum

sum = 0 # Szukana suma wyrazów ciągu Fibonacciego
a = 1   # Aktualny wyraz ciągu
b = 2   # Następny wyraz ciągu

while a <= 4000000:
	if a % 2 == 0:
		sum += a
	a, b = b, a + b

print(sum)