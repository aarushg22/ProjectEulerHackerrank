import sys

arr=[0]*(10**7)
def solve(i):
    if i==1:
        return 1
    if i<len(arr) and arr[i] is not 0:
        return arr[i]
    if i%2==0:
        if i<len(arr):
            arr[i]=solve(i//2)+1
            return arr[i]
        else:
            return solve(i//2)+1
    else:
        if i<len(arr):
            arr[i]=solve((3*i+1)//2)+2
            return arr[i]
        else:
            return solve((3*i+1)//2)+2

for i in range(2,5*(10**6)):
    if arr[i]==0:
        arr[i]=solve(i)

temp=arr[1]
for j in range(2,5*(10**6)):
    if arr[j]<temp:
        arr[j]=arr[j-1]
    else:
        temp=arr[j]
        arr[j]=j
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(arr[n])
