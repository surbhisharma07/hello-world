#Take an input year from user and decide whether it is a leap year or not.
n=int(input("enter the year"))
if(n%4==0 and n%100!=0):
    print("It is a leap year")
else:
    print("It is not a leap year")

# Take length and breadth input from user and check whether the dimensions are of square or rectangle.
l=int(input("enter length"))
b=int(input("enter breadth"))
if(l==b):
    print("It is a square")
else:
    print("It is a rectangle")

#Take the input age of 3 people and determine oldest and youngest among them.
a=int(input("enter first age"))
b=int(input("enter second age"))
c=int(input("enter third age"))
if(a>b and a>c):
    print("a is older")
elif(b>a and b>c):
    print("b is older")
else:
    print("c is older")
if(a<b and a<c):
    print("a is younger")
elif(b<a and b<c):
    print("b is younger")
else:
    print("c is younger")
#Analyse the given data
age=int(input("enter the age"))
sex=input("enter your sex")
status=input("enter your marital status")
if sex=='female':
    print("work only in urban areas.")
else:
    if age>20 and age<40:
        print("can work anywhere.")
    elif age>40 and age<60:
        print("work only on urban areas.")
    else:
        print("ERROR")

# shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user.
n=int(input("enter quantity"))
n=n*100
if n>1000:
    n=n-(n*0.1)
print("total cost : ",n)

#Loops

#Take 10 integers from user and print it on screen.
a=[]
for i in range(0,10):
    b=int(input(""))
    a.append(b)
print("List is:",a)

#Write an infinite loop.An infinite loop never ends. Condition is always true.
s=2
while s==2:
    print("HELLO")

#Create a list of integer elements by user input. Make a new list which will store square of elements of previous list.
a=[]
b=[]
for i in range(0,5):
    c=int(input(""))
    a.append(c)
    b.append(c*c)
print(a)
print(b)
#From a list containing ints, strings and floats, make three lists to store them separately
a=['hello','hi',123,33,54,20.02]
ints=[]
strings=[]
floats=[]
for i in range(0,6):
    if isinstance(a[i],int):
        ints.append(a[i])
    elif isinstance(a[i],str):
       strings.append(a[i])
    else:
        floats.append(a[i])
print("ints: ",ints)
print("strings: ",strings)
print("floats: ",floats)

#Using range(1,101), make a list containing only prime numbers.
a=[]
for j in range(1,101):
    flag=0
    if j==2:
        a.append(j)
    else:
        for i in range(2,j):
            if j%i==0:
                flag=1;
                break;
            else:
                flag=0
        if flag==0:
            a.append(j)
a.remove(1)
print(a)

#Q.6- Print the following patterns:
'''* 
   ** 
   *** 
   ****'''
for i in range(0,4):
    for j in range(0,i+1):
        print("*",end=' ')
    print("\r")
#Take inputs from user to make a list.
a=[]
for i in range(0,10):
    b=int(input(""))
    a.append(b)
b=int(input("enter number that is to be deleted"))
a.remove(b)
print(a)
