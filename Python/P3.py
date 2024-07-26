num = 600851475143
i = 2
while i*i < num: # Make this search more efficient by looking only to i^2 < N instead of brute force
    if num % i == 0: # If divisible by i continue / This means we have a factor
        num /= i # This to update num to find the next highest prime factor
        continue 
    i += 1
print(num)