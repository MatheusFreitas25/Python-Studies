lista1 = [1,2,3,4,5,6,7,8,9,10]
i = 0

for valores in lista1:
    i = i + 1
    if (valores%2 != 0) == True:
        lista1.pop(i)

print(lista1)