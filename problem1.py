#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    n=n-1
    nt1 = n//3
    nt2 = n//5
    nt3 = n//15
    ans1 = ((nt1*(2*3+(nt1-1)*3))) >> 1
    ans2 = ((nt2*(2*5+(nt2-1)*5))) >> 1
    ans3 = ((nt3*(2*15+(nt3-1)*15))) >> 1
    # print(ans3,nt3,ans2,nt2,ans1,nt1)
    print(int(ans1+ans2-ans3))


