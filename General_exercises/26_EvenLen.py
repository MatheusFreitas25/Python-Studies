str = 'Print every word in this sentence that has an even number of letters'

str = str.split()
for letter in str:
    if len(letter)%2 ==0:
        print(letter)