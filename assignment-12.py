#Q.1 Print the current day using Datetime module.

import datetime as dt
today=dt.date.today()
print("Today's date: ",today)

#Q.2 Open your browser and play a video using webbrowser module in python.

import webbrowser
g = input('Enter the video you want to search:- ')
webbrowser.open_new_tab('https://www.youtube.com/search?q=%s' %g)

#Q.3 Write a program to rename all the files in a directory and convert them into .jpg file format.

import os
path = "C:\\Users\\lenovo\\Desktop\\Daily_Assignments\\test_rename\\"
files=os.listdir(path)
i=1
for file in files:
    os.rename(os.path.join(path,file), os.path.join(path, str(i)+'.jpg'))
    i=i+1

import os
path="C:\\Users\\lenovo\\Desktop\\Daily_Assignments\\test_rename\\"
print(os.listdir(path))
