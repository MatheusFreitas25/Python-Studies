def myfunc(n):
    for i in range(1,n+1):
           print(*range(1,i+1))

x = int(input("Digite o valor : "))
myfunc(x)