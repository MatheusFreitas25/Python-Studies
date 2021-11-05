# Write a Python function to multiply all the numbers in a list

def multall(mylist):
    total = 1

    for nums in mylist:
        total = total * nums
    return total


print(multall([1, 2, 3, 3]))
