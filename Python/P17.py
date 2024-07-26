from num2words import num2words as nw
n = 1000
count = 0
for i in range(1,n+1):
    w = nw(i)
    for l in w:
        if l == " " or l == "-":
            continue
        count += 1
    print(w)

print(f"{count=}")