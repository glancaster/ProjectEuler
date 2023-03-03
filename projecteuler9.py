import random as r
import math as m
def pythagoreantriplet(data):
    a,b,c = data
    if a < b < c :
        if a**2 + b**2 == c**2:
            return True
        else:
            return False
    else:
        return False
def Sum3toM(M):
    a = r.randint(1,M-3)
    b = r.randint(1,M-a-1)
    c = M-b-a
    data = [a,b,c]
    return sorted(data)
data = [1,2,3]
while pythagoreantriplet(data) == False:
    data = Sum3toM(1000)
print(m.prod(data))