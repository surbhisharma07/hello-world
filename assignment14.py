# Print the Cube of Each Value of a List
lst=[1,2,3,4,5,6]
lst=[i**3 for i in lst]
print(lst)
# Get all the Prime Numbers in a Specific Range
a=[i for i in range(2,20)  for j in range(2,i) if(i%j==0)  ]
b=[i for i in range(2,20) if(i not in a )]
print(b)
# Differentiate Between List Comprehension and Generator Expression
'''
In terms of syntax, the only difference is that you use parenthesis instead of square brackets.
The type of data returned by list comprehensions and generator expressions differs.
The generator yields one item at a time — thus it is more memory efficient than a list.'''
# Convert the Python List to Fahrenheit
Cel = [39.2 ,36.5, 37.3, 37.8]
a=list(map(lambda x: 1.8*x+32,Cel))
print(a)

# Square all the Elements of a List
lst=[1,2,3]
def square(n):
    return n*n
s=list(map(lambda n:square(n),lst))
print(s)
# Filter out all the primes from a list
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def isprime(n):
    flag = 1
    if (n > 1):
        for i in range(2, n):

            if (n % i == 0):
                flag = 0
                break
        if (flag == 1):
            return n


p = list(filter(lambda n: isprime(n), lst))
print(p)
# Multiply all the Elements of a List
lst=[1,2,3,4,5,5]
from  functools import *
a=reduce(lambda x,y:x*y,lst)
print(a)