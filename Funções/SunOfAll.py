# Write a Python function to sum all the numbers in a list.

def sumall(my_list):
    somatotal = 0
    for nums in my_list:
        somatotal = somatotal + nums
    return somatotal


print(sumall([1, 2, 3, 4, 5]))
