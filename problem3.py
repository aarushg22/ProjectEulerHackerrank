#!/bin/python3

import sys

"""
Made for inputs upto 10^12
"""
n=10**6
prime = [True]*(n+1)
p = 2
true_primes=[]
while (p**2)<n:
    if prime[p]:
        fp=p**2
        while(fp<n):
            prime[fp] = False
            fp+=p
        true_primes.append(p)
    p+=1
for x in range(int(n**0.5), n):
    if prime[x]:
        true_primes.append(x)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    ind,ans = 0,0
    while(true_primes[ind] <= n**0.5):
        while (n % true_primes[ind]) == 0:
            n = n/true_primes[ind]
            ans = true_primes[ind]
        ind+=1
        if ind==len(true_primes): break #safety
    print(int(n if n > ans else ans))



