#Take an input year from user and decide whether it is a leap year or not.
n=int(input("enter the year"))
if(n%4==0 and n%100!=0):
    print("It is a leap year")
else:
    print("It is not a leap year")