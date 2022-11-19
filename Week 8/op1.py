def maior_elemento(lista):
	lista.sort()
	t = len(lista)-1
	return lista[t]


lista = [56, 89, 3, 190, 57]
print(maior_elemento(lista))