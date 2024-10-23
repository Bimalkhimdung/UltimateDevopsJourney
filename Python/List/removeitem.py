org = ["IT","Non-It","banking","technical"]
new_org = []

for x in org:
    print(x)

#using range
for x in range(len(org)):
    print(org[x])

#check and append it to new list if latter IT is present in org
for x in org:
    if "IT" in x:
        new_org.append(x)
print(new_org)

New_org = []


New_org =  [ x for x in org if "I" in x]
print(New_org)