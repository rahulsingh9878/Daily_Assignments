#Q.1- Create a list with user defined inputs. 
x = []
s = int(input("Enter the size of list "))
for i in range(s):
    y = input("Enter object ")
    x.append(y)
print(x)

#Q.2- Add the following list to above created list:
'''[‘google’,’apple’,’facebook’,’microsoft’,’tesla’]'''

r = ['google','apple','facebook','microsoft','tesla']
x.extend(r)
print(x)

#Q.3- Count the number of time an object occurs in a list. 
x = []
s = int(input("Enter the size of list "))
for i in range(s):
    y = input("Enter object ")
    x.append(y)
y = input("Enter object which you want to find its times of occurs ")
print(x.count(y))

#Q.4- create a list with numbers and sort it in ascending order.
x = []
s = int(input("Enter the size of list "))
for i in range(s):
    y = int(input("Enter a number "))
    x.append(y)
x.sort()
print(x)

#Q.5- Given are two one-dimensional arrays A and B which are sorted in ascending order. Write a program to merge them into a single sorted array C that contains every item from arrays A and B, in ascending order. [List] 
A=[11,20,55,66]
B=[77,99,100]
C = A+B
C.sort()
print(C)

#Q.6-Implement a stack and queue using lists.
stack = ['Rahul','Puneet']
stack.append("Raj")
print(stack)
print("After Poping")
stack.pop()
print(stack)

queue = ['Rahul','Puneet']
queue.append("Raj")
print(queue)
print("After Poping")
queue.pop()
print(queue)

#OPTIONAL QUESTION
#Q.1- Count even and odd numbers in that list.
x = []
e = 0
o = 0
s = int(input("Enter the size of list "))
for i in range(s):
    y = int(input("Enter a number "))
    if y%2==0:
        e+=1
        x.append(y)
    else:
        o+=1
        x.append(y)
print(x)
print("There are ",e," even numbers in list")
print("There are ",o," odd numbers in list")




