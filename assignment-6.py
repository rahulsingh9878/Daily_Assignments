#Q.1- Create a function to calculate the area of a sphere by taking radius from user.

def area(num):
    area=float(4*3.14*r*r)
    return area
r=int(input("Enter radius:- "))
ar=area(r)
print(ar)

#Q.2- Write a function “perfect()” that determines if parameter number is a perfect number. Use this function in a program that determines and prints all the perfect numbers between 1 and 1000. 
#[An integer number is said to be “perfect number” if its factors, including 1(but not the number itself), sum to the number. E.g., 6 is a perfect number because 6=1+2+3].

def perfect(num):
    l=0
    for i in range(1,num):
        if(num%i==0):
            l=l+i
    if(l==num):
        return l
    else:
        return 0
for i in range(1,1000):
    h=perfect(i)
    if(h!=0):
        print(h)

#Q.3- Print multiplication table of n using loops, where n is an integer and is taken as input from the user.
        
def table(n):
    for i in range(1,11):
        print(n,'X',i,'=',n*i)
n=int(input("Enter digit:- "))
table(n)

#Q.4- Write a function to calculate power of a number raised to other ( a^b ) using recursion.

def power(b,e):
    if(e==1):
        return(b)
    if(e!=1):
        return(b*power(b,e-1))
b=int(input("Enter base:- "))
e=int(input("Enter exponential value:- "))
print("Result:",power(b,e))
