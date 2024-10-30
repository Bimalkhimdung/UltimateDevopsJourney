class car:
    def __init__(self,brand,name):
        self.brand = brand
        self.name = name 
    def move(self):
        print("move")
class Boat:
    def __init__(self,brand,name):
        self.brand = brand 
        self.name = name 
    def move(self):
        print("swim")

c1 = car("tesla","model Y")
c2 = Boat("yatt","dont know")

for x in (c1,c2):
    x.move()