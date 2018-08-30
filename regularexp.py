#Write a python code to find a valid email address from a text.
import re

a = input('Enter email: ')
b = 0
c = re.finditer("^[a-zA-Z0-9]{1}[_a-zA-Z0-9.]*[@]{1}['gamil.com''yahoo.com']{9,9}$", a)
for m in c:
    b = m.group()
if a == b:
    print('Email is valid.')
else:
    print('Email is invalid.')

#Find a Valid Indian Phone Number From a Text
import re
s = input('Enter phone number: ')
m = re.finditer("^[+]{1}[9]{1}[1]{1}[6-9]\d{9}$",s)
n = 0
for i in m:
    n = i.group()
if s == n:
    print('This is a valid Indian phone number.')
else:
    print('This is not a valid Indian phone number.')