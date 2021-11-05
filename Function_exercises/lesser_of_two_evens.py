def myfunc(a,b):
    x =[a,b]
    if a % 2 == 0 and b % 2 == 0:
       return(min(x))
    else:
        return(max(x))

print(myfunc(4,120))