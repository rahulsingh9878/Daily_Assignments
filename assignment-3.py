'''                              LIST                         '''

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

#Q.6- Count even and odd numbers in that list.

l = len(C)
i=0
e=0
o=0
for i in range(l):
    if C[i]%2==0:
        e+=1
    else:
        o+=1
print("There are ",e," even numbers in list")
print("There are ",o," odd numbers in list")


'''                             TUPLES                        '''
#Q.1-Print a tuple in reverse order.
a = (1,2,3,6,4)
print(a[::-1])

#Q.2-Find largest and smallest elements of a tuples. 
a = (2,25,5,699,454)
print(max(a))
print(min(a))


'''                            STRINGS                        '''

#Q.1- Convert a string to uppercase.
a = "Rahul"
print(a.upper())

#Q.2- Print true if the string contains all numeric characters.
a = "542"
print(a.isnumeric())

#Q.3- Replace the word "World" with your name in the string "Hello World".
a = "Hello World"
a = a.replace("World","Rahul")
print(a)





