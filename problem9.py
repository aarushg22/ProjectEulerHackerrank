#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    res=-1
    for a in range(1,n):
        dividend = (n**2)-(2*n*a)
        divisor = 2*(n-a)
        if dividend%divisor == 0:
            b=dividend//divisor
            ans=int(((a**2)+(b**2))**0.5)*a*b
            res=ans if res<=ans else res
            print(a,b)
    print(-1 if res == 0 else res)
