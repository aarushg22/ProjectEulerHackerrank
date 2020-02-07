t=int(input().strip())
for _ in range(t):
    n=int(input().strip())
    tri=[]
    for _rows in range(n):
        temp=list(map(int,input().split(' ')))
        tri.append(temp)

    for rows in range(n-1):
        for col in range(n-rows-1):
            tri[n-(rows+2)][col]+=max(tri[n-(rows+1)][col],tri[n-(rows+1)][col+1])
    print(tri[0][0])
