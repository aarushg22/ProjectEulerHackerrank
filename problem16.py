# Enter your code here. Read input from STDIN. Print output to STDOUT

t=int(input().strip())
for _ in range(t):
    n=int(input().strip())
    print(sum(map(int,str(pow(2,n)))))
