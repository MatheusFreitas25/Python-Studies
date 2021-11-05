def myfunc(*args):
    my_list=[]
    for num in args:
        if num % 2 == 0:
            my_list.append(num)
            print(my_list)
    return my_list

myfunc(5,6,7,8)
