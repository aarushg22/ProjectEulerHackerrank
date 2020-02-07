
arr=[1 for i in range(1001)]
for x in range(1,1001):
    arr[x]*=(arr[x-1]*x)
t=int(input().strip())
for _ in range(t):
    n=int(input().strip())
    print(sum(map(int,str(arr[n]))))
