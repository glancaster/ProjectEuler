fibonacciSeq = [1,2] #Initialize the Fibonacci Sequence
evenFibonacciSeq = [] #Separate List for the even numbers
for x in fibonacciSeq:
    if x < 2000000:
        fibonacciSeq.append(sum(fibonacciSeq[-2:])) #Sum the previous two terms to get current term
for x in fibonacciSeq:        
    if x % 2 == 0: #Grab even valued terms from above list
        evenFibonacciSeq.append(x)
print(fibonacciSeq)
print(sum(evenFibonacciSeq))

