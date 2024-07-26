nums = []
for x in range(100,1000):
    for y in range(100,1000): #Iterate through 2 three digit numbers
        palindromicNum = str(x*y)
        if palindromicNum == palindromicNum[::-1]: #Check if it is Palindromic
            nums.append(int(palindromicNum))

print(max(nums)) #Find the largest Palindrome from a list

