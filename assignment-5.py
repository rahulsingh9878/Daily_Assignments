#Q.1- Take an input year from user and decide whether it is a leap year or not.
year = int(input("Enter Any Year:- "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(year,"is a leaf year")
        else:
            print(year,"is not a leaf year")
    else:
        print(year,"is a leaf year")
else:
    print(year,"is not a leaf year")
                     
#Q.2- Take length and breadth input from user and check whether the dimensions are of square or rectangle.
leng = int(input("Enter Length:- "))
bre = int(input("Enter breadth:- "))
if leng == bre:
    print("Entered dimensions are of Square.")
else:
    print("Entered dimensions are of Rectangle.")
            
#Q.3- Take the input age of 3 people and determine oldest and youngest among them.
age1 = int(input("Enter Your Age Person1:- "))
age2 = int(input("Enter Your Age Person2:- "))
age3 = int(input("Enter Your Age Person3:- "))
print("Oldest person  age is ",max(age1,age2,age3))
print("Youngest person age is ",min(age1,age2,age3))         

#Q.4- Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service. 

'''1. if employee is female, then she will work only in urban areas. 
2. if employee is a male and age is in between 20 to 40 then he may work in anywhere 
3. if employee is male and age is in between 40 t0 60 then he will work in urban areas only. 
4. And any other input of age should print (ERROR). '''
age = int(input("Enter Your Age:- "))
sex = input("Enter Your Sex ( M or F ):- ")
mat = input("Enter Your Marital Status ( Y or N ):- ")
if sex == "M" or sex == "m":
          if age>20 and age<40:
              print("You will work anywhere.")
          elif age>40 and age<60:
              print("You will work in urban areas.")
          else:
              print("**ERROR**")
          
else:
    print("You will work only in urban areas.")
        
          
#Q.5- A shop will give discount of 10% if the cost of purchased quantity is more than 1000.Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user.
qu = int(input("Enter the Quantity:- "))
cost = 0
if qu>1000:
         cost = qu*100
         cost = cost-cost*0.1
         print("Total Cost:- ",cost)
else:
          cost = qu*100
          print("Total Cost:- ",cost)

'''                                 LOOPS                           '''

#Q.1- Take 10 integers from user and print it on screen.
a=[]
for i in range(10):
          num = int(input("Enter a number:- "))
          a.append(num)
for i in range(10):
          print(a[i])

#Q.2- Write an infinite loop.An infinite loop never ends. Condition is always true.
while "true":
          print("HEHEHEHEHEHE")
          
#Q.3- Create a list of integer elements by user input. Make a new list which will store square of elements of previous list.
a=[]
b=[]
n = int(input("Enter the size of list:- "))
for i in range(n):
          num = int(input("Enter a number:- "))
          a.append(num)
          num*=num
          b.append(num)
print("Normal list:- ",a)
print("List after Square:- ",b)

#Q.4- From a list containing ints, strings and floats, make three lists to store them separately
string=[]
fl=[]
integer=[]
l=[4,5,6,'a','b',7,8,'r','y',4.02,6.00,]
for i in l:
    if(type(i) is str):
        string.append(i)
    elif(type(i) is float ):
        fl.append(i)
    elif(type(i) is int):
        integer.append(i)
print("List of integer type is:- ",integer)
print("List of float type is:- ",fl)
print("List of string type is:- ",string)

#Q.5- Using range(1,101), make a list containing only prime numbers.
ls=[]
for i in range(1,101):
    flag=0
    for j in range(2, int(i/2)) :
        if(i%j==0):
            flag=1
    if(flag==0):
        ls.append(i)
print(ls)
#Q.6- Print the following patterns: 
#                  * 
#                  ** 
#                  *** 
#                  **** 

patterns='*'
for i in range(1,5):
    print(i*patterns)
          
#Q.7- Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop. 
ls=[]
n=int(input("Enter the size of list:- "))
for i in range(0,n):
    num=input("Enter element:- ")
    ls.append(num)
num=input("Which element you want:- ")
ls.remove(num)
print(ls)



