pi= 22/7
try:

    radius_ = float(input("Enter the value of Radius: "))
    if type(radius_) == str:
        print("Radius value can not be string")
    else:
        volume = (4/3)*pi*((radius_)*3)

        print(f"Volume os spare is: ", volume)

except Exception as e:
    print(f"Error",{e})

