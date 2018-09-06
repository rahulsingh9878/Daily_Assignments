from functools import *

#Q.1- Write a python program to print the cube of each value of a list using list comprehension.

ls = [1,2,3,4,5,6,7,8,9]
ls1 = [x**3 for x in ls]
print(ls1)

#Q.2- Write a python program to get all the prime numbers in a specific range using list comprehension.

ls = [x for x in range(1, 20) if 0 not in[x% i for i in range(2, x)]]
print(ls)

#Q.3- Write the main differences between List Comprehension and Generator Expression.
''' Answer  '''
#A List Comprehension,executes immediately and returns a list.
#A Generator Expression,returns and object that can be iterated over.


'''                                  LAMBDA & MAP                                  '''

#Q.1- Celsius = [39.2, 36.5, 37.3, 37.8] Convert this python list to Fahrenheit using map and lambda expression.

celcius = [39.2, 36.5, 37.3, 37.8]
ls = list(map(lambda x: (x*1.8)+32, celcius))
print(ls)

#Q.2- Apply an anonymous function to square all the elements of a list using map and lambda.

Square = [1,2,3,4,5,6,7,8,9,10]
ls = list(map(lambda x: x**2, Square))
print(ls)

'''                                 FILTER & REDUCE                                 '''

#Q.1- Filter out all the primes from a list.

ls = [1,2,3,4,5,6,7,8,9,10]
def prime(n):
    for i in range(2,n):
        if n% i == 0:
            break
    else:
        return n
ls1 = list(filter(prime,ls))
print(ls1)

#Q.2- Write a python program to multiply all the elements of a list using reduce.

ls = [1, 2, 3, 4, 5]
lst = reduce(lambda x, y: x*y, ls)
print(lst)
