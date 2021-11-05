def myfunc(listnum):
    for i in range(0,len(listnum)-1):
        if listnum[i] == 3 and listnum[i+1] == 3 :
            return True
    return False

print(myfunc([1,2,3,4,3,8,3]))
