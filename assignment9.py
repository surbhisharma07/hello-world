#Name and handle the exception occured in the following program:
a = 3
if a < 4:
    try:
        a = a / (a - 3)
    except:

        print("cannot divide by zero")
    print(a)
#Output is: ZeroDivisionError

#Name and handle the exception occurred in the following program:
l=[1,2,3]
try:
    print(l[3])
except:
    print("It Is Index Error")
#Output is: IndexError

#What will be the output of the following code:
-> An exception
-> Error

#What will be the output of the following code:
-> -5.0
-> a/b result in 0

# Write a program to show and handle following exceptions:
# 1. Import Error
# 2. Value Error
# 3. Index Error

#1.IMPORT ERROR
try:
    import copyy
except ImportError as message:
    print('Exception:', message)

#2.VALUE ERROR
try:
    num=int(input("enter a number"))
except ValueError:
    print("please Enter integer value only")

#3.INDEX ERROR
l=[0,1,2,3]
try:
    print(l[4])
except:
    print("INDEX ERROR")