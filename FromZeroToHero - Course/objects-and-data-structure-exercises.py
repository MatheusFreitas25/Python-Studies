1
print("Hello World"[8])

#2
print("tinker"[1:4])
print("tinker"[2:])
print("tinker"[::-1])

#Concat, split, upper, lower, multiplicacao de string

a = "Hello World"
b = " it is a beautiful day"

c = a + b
print(c)
print(a + b)

print(c.split())
print(c.upper())
print(c.lower())
print(c * 2)

# Format

print("The result of {0} + {1} is {2}".format('10','20','30'))
print("The result of {a} + {b} is {c}".format(a='10',b='20',c='30'))
name = "Matheus"
age = 24
print(f"Hi, my name is {name} and i'm {age} years old")
print(f"Hi, my name is {name} and i'm {age:1.2f} years old")
print('i like %s' %'apples')

# list( index, Append, pop, sort, reverse) support item assignment

list = [3,2,1]
print(list)
list[0] = 10
print(list)
list.append(150)
print(list)
list.pop() #posicao que deseja remover
print(list)
list.sort()
print(list)
list.reverse()
print(list)

# dictionaries

my_dict = {'apple':1.50, 'orange':2.50, 'milk':4.0}
print(my_dict['apple'])
print(my_dict.values())
print(my_dict.items())
dict2 = {'val1':[1, 2, 3], 'val2':'text'}
print(dict2.values())
print(dict2['val2'].upper())

# Tuples(count, index), does not support item assignment

t = (1, 'Matheus', 2, 3, 4.2, 1, 1)
print(t)
print(t.count(1))
print(t.index("Matheus"))
t[0] = 2
print(t)

# sets -> unique elements
mylist = [1,2,2,2,2,2,2,3,3,3,3,4,4,44,5,5,6]
myset = set(mylist)
print(myset)
myset.add(100)
print(myset)
print(set(mylist).add(100))
name = "Matheussss"
print(set(name))

# Booleans

print(1 > 2)
print(2 == 2)
print(10 % 2 == 0)

# IO r-> read w-> write a->append

f = open("teste.txt", "w")
f.write("texto de teste!")

f = open("teste.txt", "r")
print(f.read())
print(f.readlines())

f = open("teste.txt", "a")
f.write("12345678910")

f = open("teste.txt", "r")
print(f.read())
f.close

with open("teste2.txt", "w") as f:
    f.write("teste123")