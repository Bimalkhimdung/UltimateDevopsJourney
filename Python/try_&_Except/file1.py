try:
    
    print(x)
except NameError:
    print("Exception arise Due to error !!")
except:
    print("another error")
else:
    print("Nothing wrong")
finally:
    print("this will print whether there is error or not !!")