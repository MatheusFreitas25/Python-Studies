# Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
#
#
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0


def count_evens(nums):
    x = 0
    for pos in range(len(nums)):
        if nums[pos] % 2 == 0:
            x = x + 1
    print(x)


count_evens([2, 1, 2, 3, 4])
count_evens([2, 2, 0])
count_evens([1, 3, 5])


# Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky,
# so it does not count and numbers that come immediately after a 13 also do not count.
#
#
# sum13([1, 2, 2, 1]) → 6
# sum13([1, 1]) → 2
# sum13([1, 2, 2, 1, 13]) → 6


def sum13(nums):
    x = 0
    if len(nums) > 0:
        for pos in range(len(nums)):
            if nums[pos] != 13:
                x = x + nums[pos]
        print(x)
    else:
        print("0")


sum13([1, 2, 2, 1])
sum13([1, 1])
sum13([1, 2, 2, 1, 13])


# Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array.
# Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.
#
#
# big_diff([10, 3, 5, 6]) → 7
# big_diff([7, 2, 10, 9]) → 8
# big_diff([2, 10, 7, 2]) → 8


def big_diff(nums):
    largest = nums[0]
    smallest = nums[0]
    for x in range(len(nums)):
        if nums[x] < smallest:
            smallest = nums[x]
        if nums[x] > largest:
            largest = nums[x]

    print(largest - smallest)


big_diff([10, 3, 5, 6])
big_diff([7, 2, 10, 9])
big_diff([2, 10, 7, 2])


# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and
# extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
#
#
# sum67([1, 2, 2]) → 5
# sum67([1, 2, 2, 6, 99, 99, 7]) → 5
# sum67([1, 1, 6, 7, 2]) → 4


def sum67(nums):
    aux1 = 0
    aux2 = 0
    soma1 = 0
    soma2 = 0
    for x in range(len(nums)):
        soma1 = soma1 + nums[x]
        if nums[x] == 6:
            aux1 = x
        if nums[x] == 7:
            aux2 = x
    for num in range(aux1, aux2 + 1):
        soma2 = soma2 + nums[num]
    print(soma1 - soma2)


sum67([1, 2, 2, 6, 99, 99, 7])
sum67([1, 2, 2, 6, 99, 99, 7])
sum67([1, 1, 6, 7, 2])
