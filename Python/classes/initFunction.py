# All classes have a function called __init__(), which is always executed when the class is being initiated
# Use the __init__() function to assign values to object properties

class persion:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 

p1 = persion("Bimal", 36)

print(p1.name)
print(p1.age)