i = 11*20
while all(i % x == 0 for x in range(11,21,1)) == False: # Iterates through all the divisors and if they are all true then it'll stop
    i+=20 #Increment by the highest divisor
print(i)
