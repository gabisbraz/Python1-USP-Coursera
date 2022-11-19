import math

a = int(input())
b = int(input())
c = int(input())

#equacao = (((a*x)**2)+(b*x)+c)

delta = (b**2) - 4 * a * c

if delta < 0:
	print("esta equação não possui raízes reais")


if delta == 0:
	x1 = (- b + math.sqrt(delta)) / (2 * a)
	print("a raiz desta equação é {}" .format(x1))

elif delta > 0:
	x1 = (- b + math.sqrt(delta)) / (2 * a)
	x2 = (- b - math.sqrt(delta)) / (2 * a)
	if x1 < x2:
		print("as raízes da equação são {} e {}" .format(x1, x2))
	else:
		print("as raízes da equação são {} e {}" .format(x2, x1))



