#this code will print Enter your name until you give input
#when input is given the while condition becomes false 
name=""
while len(name) == 0:
    name=input("Enter your name: ")
print("Hello",name)