#copying dictionaries from one to another
org = {
    "branch":"kathmandu",
    "abbr":"ktm",
    "code":1
}

org_ = org.copy()
print(org_)
org["code"] = 2
org["department"] = "finance" 
x_ = dict(org)

print(x_)
