def main():
	w = int(input("digite a largura: "))
	h = int(input("digite a altura: "))
	imprimeRetangulo(w, h)

def imprimeRetangulo(w, h):
	aux1 = w
	aux2 = h

	while h > 0:
		w = aux1
		while w > 0:
			if h != aux2 and h != 1 and w != aux1 and w != 1:
				print(" ", end="")
			else:
				print("#", end="")
			w -= 1
		print()
		h -= 1

main()