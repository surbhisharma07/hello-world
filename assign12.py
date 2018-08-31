#Print the Current Day
import datetime as dt
x = dt.date.today()
print(x.strftime("%A"))

#Use Webbrowser Module in Python
import webbrowser
g = input('Enter video name you want to search: ')
webbrowser.open_new_tab('https://www.youtube.com/results?search_query=%s' % g)

#Rename All the Files in a Directory And Convert Them Into .jpg File Format
import os
path = '/Users/hp/Desktop/python/hello-world/assignment12'
files = os.listdir(path)
i = 1

for file in files:
    a=input("name of file")
    os.rename(os.path.join(path, file), os.path.join(path, a+'.jpg'))
    i = i+1
