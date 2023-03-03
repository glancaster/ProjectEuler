primes = []
i = 2
def prime(i): #Determine if given number is prime or not
    if any(i % x == 0 for x in range(2,i)) == True:
        return False
    else:
        return True
while i < 2000000: #Find primes below N
    if prime(i):
        primes.append(i)
    i+=1
print(sum(primes))