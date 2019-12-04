lista1 = ['a','b','c','d','e','x','z']
lista2 = ['a','b','j','k','k','k','z']
i=[];
for elementos in lista1:
    if elementos in lista2:
        i.append(elementos)
print(i)