def remove_repetidos(lista):
	lista1 = sorted(lista)
	lista2 = []
	for i in lista1:
		if i in lista2:
			continue
		else:
			lista2.append(i)
	return lista2

lista = [1, 2, 5, 3, 4, 4]
print(remove_repetidos(lista))