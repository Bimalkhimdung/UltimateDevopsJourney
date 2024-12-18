# IT's used decorate existing function.

# this is simple step 

def decorator(func):
    def wrapper():
        print("Transcation initiated")
        func()
        print('Trasaction completed')
    return wrapper
def hello():
    print('...Executing transction')

hello1 = decorator(hello) #this hello passed as  parameter which is mapped to {func}
hello1()

#Decoration method 


