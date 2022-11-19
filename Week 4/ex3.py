n = int(input("Digite um número inteiro: "))

somador = 0

while True:
	resto = n % 10
	num = n // 10
	somador += resto
	n = num
	if num == 0:
		break

print(somador)

