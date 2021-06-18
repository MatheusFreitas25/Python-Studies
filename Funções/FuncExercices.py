# # Write a Python program to reverse a string.
#
#
# def reverseString(text):
#
#     ToList = list(text)
#     ToList.reverse()
#     ToString = "".join(ToList)
#     return ToString
#
# print(reverseString('ola ola ola'))
#
#
# Write a Python function to calculate the factorial of a number (a non-negative integer).
# The function accepts the number as an argument
#
#
def calfatorial(num):

    total = 1
    listaFatorial = [um, ]

    for posi in range(num):

        aux2 = (num - (posi + 1))
        listaFatorial.append(aux2)
    listaFatorial.pop(num)

    for num in listaFatorial:

        total = total * num

    return total


print(factorialnum(10))
