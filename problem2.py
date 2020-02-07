#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    if n < 3:
        print(2)
    else:
        a1 = 0
        a2 = 2
        an = 0
        ans = a2+a1
        while(1):
            an = a2*4 + a1 
            if(an>n): break
            ans += an
            a1 = a2
            a2 = an
        print(ans)
            

