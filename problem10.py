#!/bin/python3

import sys


n=10**6
prime = [True]*(n+1)
sol = [0]*(n+1)
p = 2
true_primes=[]
while (p**2)<n:
    if prime[p]:
        fp=p**2
        while(fp<n):
            prime[fp] = False
            fp+=p
    p+=1
for x in range(2,n):
    if prime[x]:
        sol[x]=x+sol[x-1]
    else:
        sol[x]=sol[x-1]
del prime

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(sol[n])
