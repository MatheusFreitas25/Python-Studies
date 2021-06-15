# #Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'
x = st.split()
for letter in range(len(x)):
    if x[letter][0] == 's':
        print(x[letter])

# #Use range() to print all the even numbers from 0 to 10.
even = [num for num in range(0,10) if num%2!=0]
print(even)

# #Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
dv = [num for num in range(1,51) if num%3==0]
print(dv)

#Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
word = st.split()
evstr = ['EVEN' if len(letter)%2!=0 else 'par' for letter in word]
print(evstr)

# write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz"
# instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of
# both three and five print "FizzBuzz".
for numbers in range(1,101):
    if numbers%3==0 and numbers%5==0:
        print('FizzbUZZ')
    elif numbers%5==0:
        print('Buzz')
    elif numbers%3==0 :
        print('Fizz')
    else:
        print(numbers)

#Use List Comprehension to create a list of the first letters of every word in the string below:
import distutils.util
st1 = 'Create a list of the first letters of every word in this string'
st2 = st1.split()
word1 = [word[0] for word in st2]
print(word1)
