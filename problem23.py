import math

limit=28123
prime = [True]*(limit+1)
p = 2
true_primes={}
for _d in range(limit+1):
    true_primes[_d]=False
while (p**2)<limit:
    if prime[p]:
        fp=p**2
        while(fp<limit):
            prime[fp] = False
            fp+=p
        true_primes[p]=True
    p+=1
ulimit=int(limit**0.5)
for x in range(ulimit, limit):
    if prime[x]:
        true_primes[x]=True

sum_of_abundant_nums=[0 for _ in range(3)]

def is_abundant(n):
    p=2
    total_sum=0
    un = n**0.5

    while(p<un):
        if(n%p==0):
            nbp = n//p
            total_sum += (p if p == nbp else (p+nbp))
        p+=1
    total_sum += 1
    return n < total_sum


abundant_nums=[]
abundant_nums_dict={0: False, 1:False}
for x in range(2, limit):
    abundant_nums_dict[x]=False
    if not true_primes[x]:
        if is_abundant(x):
            abundant_nums.append(x)
            abundant_nums_dict[x]=True

t = int(input().strip())
for a in range(t):
    n = int(input().strip())
    chk=0
    if n >= limit:
        print('YES')
    else:
        for ca in abundant_nums:
            if n<ca: break
            if abundant_nums_dict[n-ca]:
                print('YES')
                chk=1
                break
        if chk==0:
            print('NO')
