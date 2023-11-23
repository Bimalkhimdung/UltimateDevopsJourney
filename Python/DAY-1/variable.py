#This is a example of python variables.

a=5
b=6
c=a
First_name="Bimal"
Mid_name=""
Last_name="Rai"
print(a)
#output=5
print(c)
#output=5
print(First_name)
#output= Bimal
print(type(First_name))
#output= < class 'str' >
print((First_name) + " " + (Mid_name) + (Last_name))
#output : Bimal Rai

#Assigning Single value to multiple variable

x=y=z=50
print(x)
print(z)
print(y)

#output=50

#Assigning multiple values to multiple variables

m,n,p=10,20,30
print(m)
print(n)
print(p)

x=60 #Global variable

print(x) 

def global_v():
    global x
    print(x)
 
    x=50 #This will modify the global variable
    print(x)


global_v()
print(x) #output 50