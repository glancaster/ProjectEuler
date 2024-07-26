primes = []
i = 2
def prime(i): #Determine if given number is prime or not
    if any(i % x == 0 for x in range(2,i)) == True:
        return False
    else:
        return True
while len(primes) < 10001: #Find N Number of primes
    if prime(i):
        primes.append(i)
    i+=1

print(primes[-1:])
