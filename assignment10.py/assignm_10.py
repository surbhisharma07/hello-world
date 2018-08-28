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
num = ['4', '2', '10', '8','7','12','99','1','66','3']

with open('test.txt', 'w') as filehandle:
    for listitem in num:
        filehandle.write('%s\n' % listitem)

f=open("test.txt")
num=[]
for l in f:
    num.append(int(l))
num.sort()
f.close
with open('news.txt', 'w') as filehandle:
    for listitem in num:
        filehandle.write('%s\n' % listitem)