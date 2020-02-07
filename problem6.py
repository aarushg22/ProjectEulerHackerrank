#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    # the difference of squares is an A.P. 
    sumofsq=n+((3*n*(n-1))/2)+((2*n*(n-1)*(n-2))/6)
    sqofsum=(n*(n+1))/2
    sqofsum*=sqofsum
    print(int(sqofsum-sumofsq))
