

#Q.4- Create a class MovieDetails and initialize it with artistname,Year of release and ratings . 
'''Make methods to 
1. Display-Display the details. 
2. Add- Add the movie details. '''

class movie():
    def __init__(self):
        self.artist='NA'
        self.year='NA'
        self.rating='NA'
    def add(self,a,y,r):
        self.artist=a
        self.year=y
        self.rating=r
    def display(self):
        print("Artist:- ",self.artist," Year of release:- ",self.year," Ratings:- ",self.rating)
op=input("Do you want to add detais? Y:N \n Option:- ")
ob=movie()
if(op=='y' or op=='Y'):
    a=input("Enter artist name:- ")
    y=int(input("Enter year:- "))
    r=int(input("Enter ratings:- "))
    ob.add(a,y,r)
    ob.display()

#Q.5- Create a class Animal as a base class and define method animal_attribute. Create another class Tiger which is inheriting Animal and access the base class method.

class animal():
    def animal_attribute(self):
        print("Class animal")
class tiger(animal):
    pass
obj=tiger()
obj.animal_attribute()
    
#Q.6- What will be the output of following code.
'''class A:
        def f(self):
            return self.g()

        def g(self):
            return 'A'

    class B(A):
        def g(self):
            return 'B'

    a = A()
    b = B()
    print a.f(), b.f()
    print a.g(), b.g()'''
#Answer 6:-
"""
the output of code will generate error as the print statement doesnt have proper brackets but except that it will generate:
A B
A B
"""

#Q.7- Create a class Shape.Initialize it with length and breadth Create the method Area. Create class rectangle and square which inherits shape and access the method Area.

class shape():
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        print("Area:- ",self.l*self.b)
class square(shape):
    pass
class rectangle(shape):
    pass
l=int(input("Enter length\n"))
b=int(input("Enter breadth \n"))
if(l==b):
    obj=square(l,b)
    obj.area( )
else:
    obj=rectangle(l,b)
obj.area( )
