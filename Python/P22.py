

with open("ProjectEulerPY/0022_names.txt") as f:
    names = f.readline().split(",")

print(sorted(names[:10]))

names = sorted(names)

testlist = sorted(names[:3])

print("A", ord("A"))
print(names[937])
total = 0
for n in range(len(names)):
    v = 0
    for l in names[n][1:-1]:
        v += ord(l) - ord("A") + 1
    total += v * (n+1)
print(total)