#creating template class for employee
class employee:
    def putdata(self):
        self.id = int(input("Enter your id"))
        self.name = input("Enter you name")
        self.salary = float(input("Enter your salary"))
    def displaydata(self):
        print(self.id)
        print(self.name)
        print(self.salary)
    

# creating object
a = employee()
a.putdata()
a.displaydata()

#creating another object
b = employee()
b.putdata()
b.displaydata()

