#Q.1- Create a user defined dictionary and get keys corresponding to the value using for loop.

dis=eval(input('Enter dictionary:- '))
val=int(input('Enter the value:- '))
for key,value in dis.items():
    if val==value:
        break
print(key)

#Q.2- Create a dictionary and store student names and create nested dictionary to store the subject wise marks of every student.Print the marks of a given student from that dictionary for every subject. 
#Hint: Use nested dictionary to store subjects marks.

dis={'Rahul':{'maths':30,'PHE':30,'chem':90},'Raj':{'maths':90,'PHE':50,'chem':10},'Rachit':{'maths':78,'PHE':30,'chem':60}}
b=str(input('Enter name of student:- '))
for k,v in dis.items():
    if b==k:
        print('Maths =',dis[k]['maths'])
        print('Chem =',dis[k]['chem'])
        print('PHE =',dis[k]['PHE'])
        
