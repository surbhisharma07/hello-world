#LIST

#create a list with user defined inputs
list=[]
a=int(input("enter elements"))
for i in range(0,a):
    b=input()
    list.append(b)
print(list)

#Add the following list to the above created list:
list1=['google','apple','facebook','microsoft','tesla']
list2=[]
list2=list+list1
print(list2)

#count the number of times an object occurs in the list
#taking 'list2' as our base object
c=input("enter the object")
print(c," ","occurs"," ",list2.count(c)," times")

#create a list and sort them in ascending order
list3=['2','1','7','6','5']
list3.sort()
print(list3)

#merge two arrays and sort it:
a=['1','3','2','4']
b=['7','6','9','0']
c=a+b
c.sort()
print(c)

#count even and odd number in the list
a=[]
e=0
o=0
b=int(input("enter no. of elements"))
for i in range(0,b):
    c=int(input(" "))
    a.append(c)
    if c%2==0:
        e=e+1
    else:
        o=o+1
print("number of even numbers are:",e)
print("number of odd numbers are:",o)

#TUPLES

#reverse a tuple
a=(5,6,7,8,9)
b=slice(-1,-5,-1)
print(a[b])

#find largest and smallest elements in tuples
tuple=(6,4,5,8,9)
a=max(tuple)
b=min(tuple)
print("maximum element is",a)
print("minimum element is",b)

#STRINGS

#convert a string into upper case
str="Be Yourself"
str1=str.upper()
print(str1)

#print true if the string contains all numeric characters.
num='18851877'
if num.isdigit():
    print("TRUE")
else:
    print("FALSE")

#Replace the word "world" with your name in the string"Hello World".
str="Hello World"
str1=str.replace("World","Surbhi")
print(str1)