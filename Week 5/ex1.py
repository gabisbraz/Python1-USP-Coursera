def maximo(x, y):
	if x >= y:
		return x
	else:
		return y
		
x = int(input())
y = int(input())
print(maximo(x, y))