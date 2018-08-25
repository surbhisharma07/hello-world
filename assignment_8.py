#Classes and Object

#Calculate Area and Circumference of a Circle
class circle:
    def __init__(self,b):
        self.radius=b
    def getArea(self):
        return(3.14*self.radius*self.radius)
    def getCircumference(self):
        return(2*3.14*self.radius)
b=int(input("enter radius :"))
a=circle(b)
print("Area is ",a.getArea())
print("circumference is ",a.getCircumference())

#Make a Class Student and Display its Required Info
class student:
    def __init__(self):
        self.name = input()
        self.roll = int(input())

    def setAge(self):
        self.age = int(input())

    def setMarks(self):
        self.marks = int(input())

    def display(self):
        print("name =", self.name, " rollno =", self.roll, " age =", self.age, " marks =", self.marks)
s = student()
s.setAge()
s.setMarks()
s.display()

#Convert Temperature
class temperature:
    def convertFahrenheit(self):
        self.cel=int(input("enter temperature in celsius"))
        return((9/5)*self.cel+32)
    def convertCelsius(self):
        self.far=int(input("enter temperature in Fahrenheit"))
        return(((self.far-32)*5)/9)
temp=temperature()
print(temp.convertFahrenheit())
print(temp.convertCelsius())

#Create a Class MovieDetails and Perform the Required Functionalities
class Movie:
    def __init__(self,aname,year,ratings):
        self.aname=aname
        self.year=year
        self.ratings=ratings
    def add(self,name):
        self.name=name
        print(self.name)
    def display(self):
        print("{} {} {}".format(self.aname,self.year,self.ratings))
a=input("enter name")
b=input("enter year")
c=int(input("enter ratings"))
d=Movie(a,b,c)
name=input("enter movie name")
d.add(name)
d.display()
#Inheritance(Animal)
class Animal:
    def animal_attribute(self):
        return 'TIGER IS HERE'
class Tiger(Animal):
        pass
b = Tiger()
print(b.animal_attribute())

#Determine the Output
"Output is:ERROR"

#Inheritance(Shapes)
class shape:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        return(self.length*self.breadth)
class rectangle(shape):
    pass
class square(shape):
    pass
l=int(input("enter length"))
b=int(input("enter breadth"))
r=rectangle(l,b)
s=square(l,b)
print("area of rectangle ",r.area())
print("area of square ",s.area())