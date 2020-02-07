import sys
"""
Used Dynamic programming but the basic math behind this is
Pascals Triangle. Using Dp here just creates a Pascals Triangle
"""
limit =501
m=(10**9)+7
arr=[[0 for _ in range(limit)]for _ in range(limit)]
for i in range(limit):
    for j in range(limit):
        if i==0 or j==0:
            arr[i][j]=1
        else:
            arr[i][j]=(arr[i-1][j]+arr[i][j-1])%m

t=int(input().strip())
for _ in range(t):
    n,m = input().strip().split(' ')
    n,m = [int(n),int(m)]
    print(arr[n][m])
