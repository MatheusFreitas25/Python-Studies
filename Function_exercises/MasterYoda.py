def myfunc(name):
    x = name.split()
    y =x[0]
    x[0]=x[2]
    x[2]=y

    return ' '.join(x)
print(myfunc('I am home'))
