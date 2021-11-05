def myfunc(word):
    a = []
    for i in range(0,len(word)):
        a += word[i]*3
    return ''.join(a)

print(myfunc('Hello World'))