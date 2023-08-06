import time
st = time.time()
n = pow(10,4)
m = pow(10,4)*5
print(f"Brute S({n},{m})")

s = [x for x in range(2,n+1)]
def rounds(s1,m1):
    i = 0
    for i in range (m1):
        v = min(s1)
        ind = s1.index(v)
        s1[ind] = pow(v,2)
        if i%10000 == 0:
            print(f'Iter: {i}')
    return s1 

print("ANS: ",sum(rounds(s,m))%1234567891)
print(f"Exe time: {time.time()-st} ")
