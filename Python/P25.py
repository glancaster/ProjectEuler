from itertools import permutations

n = 9
per = [m for m in range(n+1)]
print(per)
lex = [p for p in permutations(per)]
print(lex[999999])