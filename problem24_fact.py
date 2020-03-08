import math

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    n_c = n
    pos = [13,12,11,10,9,8,7,6,5,4,3,2,1]
    d = {13:'a',12:'b',11:'c',10:'d',9:'e',8:'f',7:'g',6:'h',5:'i',4:'j',3:'k',2:'l',1:'m'}

    nf=1
    for nf in range(1,14):
        if math.factorial(nf) >= n_c: break

    res = []
    if n_c == 1:
        print('abcdefghijklm')
    elif n_c == 2:
        print('abcdefghijkml')
    elif n_c == 3:
        print('abcdefghijlkm')
    else:
        n_c-=1
        if math.factorial(nf) == n_c:
            res = pos[-nf:]
            res = res[::-1]
        else:
            num = nf-1
            sub_pos = pos[-(num+1):]
            count=0
            for x in range(num,0,-1):
                if x == 1:
                    res.append(sub_pos[n_c])
                    del sub_pos[n_c]
                    break
                div = math.factorial(x)
                count = n_c // div
                # print(n_c, div, count, sub_pos)
                res.append(sub_pos[count])
                del sub_pos[count]
                n_c = n_c - (count*div)
            res.append(sub_pos[0])
        res = pos[:-nf]+res
        sol=''
        for i in res:
            sol+=d[i]
        print(sol)
