import copy as c

# Q.1 - Reverse the whole list using list methods.

a = int(input("Enter the number of elements "))
list = []
for i in range(a):
    num = int(input("Enter the element "))
    list.append(num)
print(list)
print("Reversed list: ")
list.reverse()
print(list)

# Q.2 - Print all the uppercase letters from a string.

a = input("Enter string ")
print("Characters in upperCase are:- ")
for i in a:
    if i.isupper():
       print(i) 

# Q.3 - Split the user input on comma's and store the values in a list as integers

a = input("Enter the numbers with commas in between\n")
ls = []
ls = a.split(",")
print("List: ", ls)

# Q.4 - Check whether a string is palindromic or not.

a = input("Enter a string: ")
rev = a[::-1]
if a == rev:
    print("String is Palindrome")
else:
    print("String is not Palindrome")

# Q.5- Make a deepcopy of a list and write the difference between shallow copy and deep copy.
'''                                  DeepCopy                                        '''

a = [99, 30, [40, 52, 75], 63, 74]
b = c.deepcopy(a)
print('List1: ', a)
print('List2: ', b)
b[2][0] = 15
print('After changing List2')
print('List1: ', a)
print('List2: ', b)

'''                                ShallowCopy                                     '''

a = [99, 30, [40, 52, 75], 63, 74]
b = c.copy(list1)
print('List1: ', a)
print('List2: ', b)
b[2][0] = 16
b[2][1] = 5
print('After changing List2')
print('List1: ', a)
print('List2: ', b)

# DIFFERENCE

''' 1.Changes made in deep copy of a list are never reflected in the original list
 where as changes made in shallow copy of a list are always reflected in original list.
 2.In deepcopy of object is copied to other object where as in shallow copy
 reference of object is copied in other object  '''
