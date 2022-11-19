def maior_elemento():
	lista = []
	while True:
		n = int(input("Digite um número: "))
		if n == 0:
			break
		else:
			lista.append(n)

	lista.reverse()

	#print(lista)
	for num in lista:
		print(num)

maior_elemento()