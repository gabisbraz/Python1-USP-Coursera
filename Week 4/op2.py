n = int(input("Digite um número inteiro: "))

restoAntes = " "

while True:
	resto = n % 10
	if resto == restoAntes:
		print("sim")
		break
	num = n // 10
	n = num
	restoAntes = resto
	if num == 0:
		print("não")
		break

