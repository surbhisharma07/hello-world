#Write a Python program to read n lines of a file
a=open('python.txt','r')
b=a.readlines()
for i in b:
    print(i)
a.close()

#Write a program to count the frequency of words in a file
from collections import Counter
with open('python.txt','r') as a:
    b=Counter(a.read().split())
    print(b)


#Write the program to copy the contents of the file to the another file
with open('python.txt','r') as a:
    with open('python1.txt','w') as c:
        for i in a:
            c.write(i)
#Write a Python program to combine each line from first file with the corresponding line in second file
with open('python.txt') as a:
    with open('text.txt') as b:
        for l1,l2 in zip(a,b):
            print(l1+l2)

#To write random number into the file.Sort it and store in the another file.
file=open("lmn.txt")
column=[]
for i in file:
    column.append(int(i))
column.sort()
print(column)
file.close()