def myfunc(a,b,c):
    if sum((a,b,c))<=21:
        return sum((a,b,c))
    elif sum((a,b,c))>21 and 11 in (a,b,c):
        return sum((a,b,c))-10
    else:
        return 'BURST'

print(myfunc(10,11,10))