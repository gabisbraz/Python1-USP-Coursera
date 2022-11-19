def main():
	w = int(input("digite a largura: "))
	h = int(input("digite a altura: "))
	imprimeRetangulo(w, h)

def imprimeRetangulo(w, h):
	aux = w
	while h > 0:
		w = aux
		while w > 0:
			print("#", end="")
			w -= 1
		print()
		h -= 1

main()