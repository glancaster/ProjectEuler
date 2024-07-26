
def sumdivs(n):
    d = set()
    for i in range(1, int(n//2)+1):
        if n%i==0:
            d.add(i)
    return sum(d)
# n = 220
# m = sumdivs(n)
# print(sumdivs(m) == n)
anums = set()
n = 10000
for m in range(1,n+1):
    f = sumdivs(m)
    if f == m:
        continue
    if sumdivs(f) == m:
        anums.add(m)
        if f < n:
            anums.add(f)

print(sum(anums))