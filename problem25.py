<<<<<<< HEAD
limit=5000
=======
mit=5000
>>>>>>> 30af2b7ee32e247949aa73a518a08fb564ca3b92
n_digits=[0 for _ in range(limit+1)]
f,s=1,1
t=0
n_digits[1]=1
tn=2
ln=0
while(ln<=limit):
    t=f+s
    f=s
    s=t
    tn+=1
    ln=len(str(t))
    if n_digits[ln]==0:
        n_digits[ln]=tn
    if ln==limit: break

t=int(input().strip())
for _test in range(t):
    n=int(input().strip())
    print(n_digits[n])
