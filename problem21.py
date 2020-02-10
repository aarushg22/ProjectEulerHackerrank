import math

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

del prime
d_vals=[0 for _d in range(n+2)]
# print(n)

def d(n):
    # print(n)
    p=2
    total_sum = 0
    if n>len(d_vals)-1:
        total_sum=0
        while(p**2<n+1):
            if(n%p==0):
                total_sum += p + n//p
            p+=1
        return total_sum + 1
    else:
        if d_vals[n] is 0:
            while(p**2<n+1):
                if(n%p==0):
                    total_sum += p + n//p
                p+=1
            d_vals[n] = total_sum + 1
        return d_vals[n]


# cumm_amicable = [0 for _ in range(220)]
amicable=[]
for x in range(220, n+1):
    if x in amicable:
        continue
    tmp = d(x)
    if d(tmp) == x and not tmp == x:
        amicable.append(tmp)
        amicable.append(x)
    #     cumm_amicable.append(cumm_amicable[-1]+x)
    # else:
    #     cumm_amicable.append(cumm_amicable[-1])
amicable.sort()
# print(amicable)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    ans=0
    for a in amicable:
        if a>n:
            break
        ans+=a
    print(ans)
