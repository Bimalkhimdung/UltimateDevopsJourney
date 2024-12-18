class Persion:
    def __init__(this_is_test_self,name,age,address):
        this_is_test_self.name = name 
        this_is_test_self.age = age
        this_is_test_self.address = address
    def __str__(another_self):
        return f"Your Name is {another_self.name} and age is {another_self.age} Live in {another_self.address}"

p_ = Persion("Bimal",27,"Jhapa")

print(p_)

