#!/bin/python3

import sys

n=40
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
    ans,ind=1,0
    temp_ans=1
    p =true_primes[ind]
    while(p<=n):
        temp_ans=1
        while(temp_ans<=n):
            temp_ans*=p
        temp_ans//=p
        ind+=1
        p =true_primes[ind]
        ans*=temp_ans
    print(ans)
