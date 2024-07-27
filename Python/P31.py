from time import sleep


total = 5
coins = [5,2,1]

options = []
i = 0
c = 1
stack = [coins[0]]
while len(stack) or i < 20:
    print(stack)
    if sum(stack) == total:
        options.append(stack)
        stack.append(coins[c])
    elif sum(stack) > total:
        stack.pop(0)
    elif sum(stack) < total:
        stack.append(coins[c])
        c+=1
    sleep(1)
    i += 1