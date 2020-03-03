def myfunc(name):
    out = []
    for i in range(len(name)):
         if i % 2 == 0:
            out.append(name[i].upper())
         else:
            out.append(name[i].lower())
    return ''.join(out)

myfunc('matheus')


