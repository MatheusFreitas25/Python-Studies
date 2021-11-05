def oldmacdonald(name):
    x = []
    for i in range(len(name)):
        if i == 0 or i == 3:
            x.append(name[i].upper())
        else:
            x.append(name[i])
    return ''.join(x)

print(oldmacdonald('macdonald'))