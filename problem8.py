#!/bin/python3

import sys

def movingProd(num, i , j):
    prod=1
    for x in range(i,j):
        prod *= int(num[x])
    return prod

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    moving_prod=1
    ans=0
    z_count=0
    for i in range(0,k):
        if int(num[i])==0: z_count+=1
        moving_prod *= int(num[i])
        # print(moving_prod,"s")
    ans = moving_prod
    for j in range(k,n):
        if int(num[j-k])==0:
            z_count-=1
            if z_count==0:
                moving_prod = movingProd(num,j-k+1,j)
            else:
                moving_prod = 0
        else:
            moving_prod //= int(num[j-k])
        moving_prod *= int(num[j])
        if int(num[j])==0: z_count+=1
        # print(moving_prod,"m")
        ans = moving_prod if moving_prod > ans else ans
    print(ans)
