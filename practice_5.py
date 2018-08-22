#Create a function to calculate the area of a sphere by taking radius from user.
def calc(r):
    return(4*3.14*r*r)
r=int(input("enter a radius"))
print(calc(r))

#Print multiplication table of n using loops, where n is an integer and is taken as input from the user.
def mul(a):
    for i in range(1,11):
        print(n,"*",i,"=",(n*i))
a=int(input())
mul(a)