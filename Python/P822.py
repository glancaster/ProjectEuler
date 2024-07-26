n = pow(10,1)
m = pow(10,2) + 1

print(f"S({n},{m})")

s = [x for x in range(2,n+1)]
l = s.copy()
exp = [1]*(n-1)

def rounds(s1,n1,m1):
    expdiv = m1 // n1
    rem = (n1-1) - ((m1) % (n1-1))
    r = 1
    while r < rem + 3:
        v = min(s1)
        ind = s1.index(v)
        s1[ind] = v*v 
        exp[ind] *= 2
        r+=1
    finalexp = [x*pow(2,expdiv) for x in exp]
    finallist =[]
    for i in range(len(l)):
        finallist.append(pow(l[i], finalexp[i], 1234567891))
    
    print(sum(finallist) % 1234567891)

rounds(s,n,m)