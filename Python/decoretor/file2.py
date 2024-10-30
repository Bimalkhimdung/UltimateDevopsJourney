def upper(text):
    return text.upper()
def lower(text):
    return text.lower()

def greet(func):
    greetings = func("HI i am bimal ")
    print(greetings)

greet(upper) # Here greet taking function upper as an argument
greet(lower)
