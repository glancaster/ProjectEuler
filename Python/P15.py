n = 20
# i = 0
# routes = [[1,0]] #by setting it to 1,0 you reduce half the search space
# while i < 2*n:
#     if routes[0] == [n,n]:
#         break
#     route = []
    
#     for r in routes:
#         x,y = r
#         if x < n:
#             route.append([x+1,y])
#         if y < n:
#             route.append([x,y+1])
    
#     routes = route
#     i +=1
    
# print(2*len(routes))
    
# from itertools import permutations

# moves = [0]*n + [1]*n
# print(moves)
# uniquemoves = set(permutations(moves))
# print(len(uniquemoves))

def fact(n):
    for i in range(1,n):
        n*=i
    return n

res = fact(2*n)/(fact(n)*fact(n))
        
print(res)