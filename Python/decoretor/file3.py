def hello_decorator(fun):
    def before_func():
        print("This prints before decorator function")
        fun()

    
        print("This prints after decorator function")

    return before_func

def decorator_func():
    print(" This is inside decorator function")

decorator_func = hello_decorator(decorator_func)

decorator_func()