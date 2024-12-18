count = 0
while True:
    count+=1
    if count == 5:
    #this will skip 5 for printing
        continue
    #limit count to 10
    if count > 10:
        break
    print(count)