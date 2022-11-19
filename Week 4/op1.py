n = int(input("Digite um número inteiro: "))

i = 2
result = True

while i < n-1:
    if n % i == 0:
        result = False
        print("não primo")
        break
    i += 1

if result == True:
    print("primo")