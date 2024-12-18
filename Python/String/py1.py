# simple string
_str="Hello from python string"

print(_str)

for str in range(len(_str)):
    print(_str[str])

#will print H and p
print(_str[0], _str[11])

#print last string
print(_str[-1])

#Deleting and reassigning strigns is not possible
# str = "HELLO"
# str[0] = "h"
# print(str)
_first="Bimal"
_last="khimdung"
full_name=((_first+" "+_last))
full_name_=[full_name[-1]]

print(full_name_)
#print boolen true or false for string
print( 'B' in full_name )
print('B' not in full_name)

print("first line \
      second line \
      third line ")
print("hello\nworld")