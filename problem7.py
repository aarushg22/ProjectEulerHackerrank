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

#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(true_primes[n-1])
