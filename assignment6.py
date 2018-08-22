#Create a function to calculate the area of a sphere by taking radius from user.
def calc(r):
    return(4*3.14*r*r)
r=int(input("enter a radius"))
print(calc(r))

#Perfect Number
def per(a,b):
    for i in range(a,b):
        sum=0
        for j in range(1,i):
            if(i%j==0):
                sum=sum+j
        if(sum==i):
            print(i,end=" ")
per(1,1000)

#Print multiplication table of n using loops, where n is an integer and is taken as input from the user.
def mul(a):
    for i in range(1,11):
        print(a,"*",i,"=",(a*i))
a=int(input("enter number"))
mul(a)


#power with recursion
def pow(a,b):
    if(b==1):
        return a
    else:
        return a*pow(a,b-1)

a=int(input())
b=int(input())
print(pow(a,b))

