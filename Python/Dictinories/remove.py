org = dict(code=1,branch="kathmandu",abbr="ktm")
org.popitem()
print(org)

org["abbr"]= "ktm"

print(org)

del org["abbr"]

print(org)

#to clear all dictionery items
#org.clear()