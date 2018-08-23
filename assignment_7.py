#Get keys corresponding to a value in user defined dictionary
a={}
for i in range(1,5):
    k=input("enter the key")
    v=int(input("enter a value"))
    a[k]=v
print(a)
#Nested Dictionary
a={}
b={}
for i in range(1,3):
    b={}
    name=input("enter the name")
    for j in range(1,3):
        sub=input("enter subject")
        marks=int(input("enter marks"))
        b[sub]=marks
    a[name]=b
print(a)
stu=input("enter the student name whose number you want to see")
print(a[stu])