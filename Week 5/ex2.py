def maior_primo(num):
	min = 2
	while min != num:
		cont = 1
		div = 0
		while cont <= num:
			if num % cont == 0:
				div += 1
			cont += 1
			if div > 2:
				break
		if div == 2:
			return num
		num -= 1

num = int(input())
print(maior_primo(num))