naturalNum = [] #Initialize an empty list
for i in range(1,1000): 
    if i % 3 == 0: #If divisble by 3 append to naturalNum list
        naturalNum.append(i)
    elif i % 5 == 0: #If divisble by 5 append to naturalNum list
        naturalNum.append(i)
    
print(sum(naturalNum))