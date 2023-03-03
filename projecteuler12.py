i = 1
tri = 0
triangleNum = []
def numfactors(n):
    i = 1
    nfactors = 0
    while i < n + 1:
        if n % i == 0:
            nfactors += 1
        i+=1
    return nfactors
divisors = 0
while divisors < 500:
    tri += i
    divisors = numfactors(tri)
    triangleNum.append(divisors)
    i+=1
print(tri)
print(triangleNum)