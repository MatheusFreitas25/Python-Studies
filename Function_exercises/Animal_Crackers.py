def myfunc(word):
    x = word.split()
    if x[0][0].lower() == x[1][0].lower():
        return True
    else:
        return False

print(myfunc('Lhama Horse'))