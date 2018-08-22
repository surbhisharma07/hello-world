#Reverse whole list using list methods
a=[3,4,5,6]
b=a[::-1]
print(b)

#Print all the uppercase letters from a string
a="BE YOUrseLf"
for i in a:
    if(i.isupper()):
        print(i)

#Split and Store the value after typecasting
a=input("enter a string")
b=[]
for i in a:
    b=a.split(",")
print(b)


#check for pallindrome
a=input("enter a string")
if(a==a[::-1]):
    print("It is a palindrome")
else:
    print("It is not a palindrome")

#understand deep and shallow copy
#deep copy
import copy
a=[5,6,[3,4],2]
b=copy.deepcopy(a)
a[2][0]="Three"
print(a)
print(b)
#A deep copy creates a new object and recursively adds the copies of nested objects present in the original elements.

#shallow copy
import copy
a=[5,6,[3,4],2]
b=copy.copy(a)
a[2][0]="Three"
print(a)
print(b)
#A shallow copy creates a new object which stores the reference of the original elements.
