
pathtest = [3,
            7,4,
            2,4,6,
            8,5,9,3]
path =[75,
       95,64,
       17,47,82,
       18,35,87,10,
       20,4,82,47,65,
       19,1,23,75,3,34,
       88,2,77,73,7,63,67,
       99,65,4,28,6,16,70,92,
       41,41,26,56,83,40,80,70,33,
       41,48,72,33,47,32,37,16,94,29,
       53,71,44,65,25,43,91,52,97,51,14,
       70,11,33,28,77,73,17,78,39,68,17,57,
       91,71,52,38,17,14,91,43,58,50,27,29,48,
       63,66,4,68,89,53,67,30,73,16,69,87,40,31,
       4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]

def ppath(path):
    tri = []
    l = len(path)
    i = 0
    n = 1
    while n + i <= l:
        ele = path[i:n+i]
        tri.append(ele)
        i=n+i
        n+=1
    return tri
tri = ppath(path)


def possibleroutes(n):
    routes = []
    def routing(s,p):
        if len(p) == n:
            routes.append(p)
            return
        routing(s+1,p+[s+1])
        routing(s,p+[s])
    
    routing(0,[0])
    return routes

# routes = possibleroutes(len(tri))
routes = possibleroutes(100)


# m = 0
# for r in routes:
#     i = 0
#     s = 0
#     for l in tri:
#         s += l[r[i]]
#         i +=1
#     if s > m:
#         m = s

# print(m)



# routes = []
# route = []
# i = 1
# b = 0
# while (1):
#     if ll == ind:
#         b = 1
#     e = 0
#     for l in tri:
#         route.append(l[ll[e]])
#         e+=1
#     if ll[e-i] == 0:
#         i = 1
#     ll[e-i] -=1
#     i +=1
#     routes.append(route)
#     route=[]
#     if b == 1:
#         break

# ll = [len(l)-1 for l in tri]
# i = 1
# b = 0
# while (1):
#     if ind == ll:
#         b = 1
#     e = 0
#     for l in tri:
#         route.append(l[ind[e]])
#         e+=1
#     if ind[e-i] == ll[e-i]:
#         i = 1
#     ind[e-i] +=1
#     i+=1

#     if route not in routes:
#         routes.append(route)
#     route=[]
#     if b == 1:
#         break
# print(max([sum(r) for r in routes]))
# # for t in tri:
# #     print(t,len(t))













# r = tri[0]
# for l in range(len(tri)-1):
#     s = []
#     for e in range(len(tri[l])):
#         print(l,e, [r[e], tri[l+1][e]], [r[e], tri[l+1][e+1]])
#         left = r[e] + tri[l+1][e]
#         right = r[e] + tri[l+1][e]
#         s.append(left)
#         s.append(right)
#     r = s





