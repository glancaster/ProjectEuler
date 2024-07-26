import pandas as pd
import numpy as np

df = pd.read_fwf('data11.txt',sep = '', header = None)
#print(df)

greatestprod = 0
#left right
for i in range(17):
    for j in range(20):
        l = [df[i][j],df[i+1][j],df[i+2][j],df[i+3][j]]
        prod = np.prod(l)
        greatestprod = max(greatestprod,prod)

#up down
for j in range(17):
    for i in range(20):
        l = [df[i][j],df[i][j+1],df[i][j+2],df[i][j+3]]
        prod = np.prod(l)
        greatestprod = max(greatestprod,prod)

#diagonal down right
for j in range(17):
    for i in range(17):
        l = [df[i][j],df[i+1][j+1],df[i+2][j+2],df[i+3][j+3]]
        prod = np.prod(l)
        greatestprod = max(greatestprod,prod)
#diagonal down left
for j in range(17):
    for i in range(17):
        l = [df[i][j+3],df[i+1][j+2],df[i+2][j+1],df[i+3][j]]
        prod = np.prod(l)
        greatestprod = max(greatestprod,prod)
print(greatestprod)



