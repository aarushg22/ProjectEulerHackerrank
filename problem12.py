#!/bin/python3

import sys

"""
Reference for the math behind the solution
https://www.math.upenn.edu/~deturck/m170/wk2/numdivisors.html
"""
n=10**5
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

ans=1
i=1
sol=[(1,1)]
while ans<=1000:
    ind=0
    ans,prev,sum_of_powers=1,0,0
    n=(i*(i+1))//2
    n_c=n
    temp=[]
    while(n>1):
        while n%true_primes[ind]==0:
            sum_of_powers+=1
            n//=true_primes[ind]
        if sum_of_powers is not 0:
            ans*=sum_of_powers+1
        sum_of_powers=0
        ind+=1
    # print(ans,n_c)
    temp=[]
    i+=1
    if ans>sol[-1][1]:
        sol.append((n_c,ans))

# print(sol)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    for x in sol:
        if n < x[1]:
            print(x[0])
            break
