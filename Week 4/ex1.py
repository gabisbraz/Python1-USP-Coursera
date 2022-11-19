n = int(input())
if n == 2:
    print(2)
elif n == 1 or n == 0:
    print(1)
else:
    cont = n - 1

    while cont != 1:
        multi = n * cont
        cont -= 1
        n = multi

    print(multi)