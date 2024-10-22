org = dict(branch="kathmandu", abbr="ktm",code=1)

for x in org:
   print(x)
#print all values
# for x in org:
    # print(x,org[x])
#Output
# branch kathmandu
# abbr ktm
# code 1

# for x in org.values():
    # print(x)
# 
#to get values of keys
for x in org.keys():
    print(x)
for x, y in org.items():
    print(x,y)