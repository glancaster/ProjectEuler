maxn = 0
coe = []

def isprime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

bprimes = [b for b in range(-1000,1001) if isprime(abs(b))]

print(bprimes)

for a in range(-999, 1000):
    for b in bprimes:
        print([a,b], maxn, coe)
        n = 0
        while isprime(n*n + a*n + b):
            n+=1
        if n > maxn:
            maxn = n
            print(n)
            coe = [a,b]
print(maxn, coe)     
            