def n_primos(num):
	min = 2
	nPrimos = 0
	while min <= num:
		cont = 1
		div = 0
		while cont <= num:
			if num % cont == 0:
				div += 1
			cont += 1
			if div > 2:
				break
		if div == 2:
			nPrimos += 1
		num -= 1
	return nPrimos

num = int(input())
print(n_primos(num))