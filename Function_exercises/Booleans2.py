def myfunc(x,y,z):
    if z == True:
        return x
    elif z == False:
        return y

a = myfunc('Hello','Bye',True)
print(a)