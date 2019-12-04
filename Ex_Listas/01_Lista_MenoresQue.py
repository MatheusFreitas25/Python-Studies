a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
c = int(input("Os numeros devem ser menores do que : "))
b=[]
for elem in a:
    if elem < c:
        b.append(elem)
        print(elem)

print(b)