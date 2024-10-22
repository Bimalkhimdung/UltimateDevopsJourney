org = {
   "realhrsoft": { 
    "branch":"kathmandu",
    "department":"Development",
    "code":1
},
    "aayulogic":{
    "branch": "lalitpur",
    "department": "devops",
    "code": 2
    }
}
# print(org["realhrsoft"])
# print(org["aayulogic"])
for x in org["realhrsoft"].values():
    print(x)
for x in org["aayulogic"].keys():
    print(x)
for x, y in org(["aayulogic"],["realhrsoft"]):
    print(x,y)
