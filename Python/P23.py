def sumdivs(n):
    d = set()
    for i in range(1, int(n//2)+1):
        if n%i==0:
            d.add(i)
    return sum(d)


n = 28123

a = []

for i in range(1,n):
    if sumdivs(i) > i:
        a.append(i)
print(a)

sumof2a = set()
for i in a:
    for j in a:
        sumof2a.add(i + j)

print(sumof2a)

pi = 0

for m in range(1,n):
    if m not in sumof2a:
        pi += m
print(pi)