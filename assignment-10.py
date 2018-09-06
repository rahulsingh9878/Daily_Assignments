f=open("Rahul.txt",'w')
f.write("hi")
f.write("\n hello")
f.write("\n up")
f.write("\n hi")
f.write("\n below")
f.write("\n hello")
f.write("\n werty")
f.write("\n hi")
f.write("\n hello")
f.close()
#Q.1- Write a Python program to read n lines of a file

f=open("Rahul.txt",'r')
lines = f.readlines()
n=int(input('No. of lines you want to read:- '))
print(lines[:n])

#Q.2- Write a Python program to count the frequency of words in a file.

from collections import Counter
with open('Rahul.txt') as t:
    word=Counter(t.read().split())
    print(word)

#Q.3- Write a Python program to copy the contents of a file to another file

f2 = open('output.txt', 'w')
for l in lines:
    f2.write(l)
f2.close() 
    
#Q.4- Write a Python program to combine each line from first file with the corresponding line in second file.

f2 = open('output.txt', 'a')
f3 = open('Rahul.txt', 'r')
for l in lines:
    li = f3.readline()
    f2.write(l + li)
f2.close()
f3.close()

#Q.5- Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers and then store it to another file.
import random
import random as r
f=open("number.txt",'w')
for i in range(0,10):
    a=r.randint(1,9)
    f.write(str(a)+"\n")
f.close()
f=open("number.txt",'r')
a=f.readlines()
f.close()
f=open("sort_file.txt",'w')
a.sort()
for i in range(len(a)):
    f.write(a[i])
f.close()
