def MaxOfThree(my_list):
    max = 0
    for nums in my_list:
        if nums > max:
            max = nums
    return max


print(MaxOfThree([10, 200, 3]))
