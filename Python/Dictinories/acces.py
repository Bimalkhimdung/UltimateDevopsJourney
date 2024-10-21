org = dict(code=1,branch="kathmandu",abbr="ktm")
x_ = org.keys()
print("values of keys:",x_)

y_ = org.get("code")
print("code", y_)

z_ = org.get("branch")
print("Your Branch is ", z_)

a_ = org.values()
print(a_)
print(org.values())

b_ = org.items()
print(b_)

#check if code exits
if "code" in org:
    print("yess!!!")
elif:
    print("Ohhu nouu !!")
