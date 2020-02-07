"""
Made merge sort myself from scratch because wanted to practice and
see if i still remember the algorithm correctly. :)
"""
def merge(arr, l, m, r):
    il, ir, ind=0,0,l
    tmp1=[arr[i] for i in range(l,m+1)]
    tmp2=[arr[i] for i in range(m+1,r+1)]
    while(ind<=r):
        if il==len(tmp1):
            arr[ind]=tmp2[ir]
            ir+=1
        elif ir==len(tmp2):
            arr[ind]=tmp1[il]
            il+=1
        else:
            if tmp1[il]<tmp2[ir]:
                arr[ind]=tmp1[il]
                il+=1
            else:
                arr[ind]=tmp2[ir]
                ir+=1
        ind+=1

def mergeSort(arr, l, r):
    if l<r:
        m=(l+r)//2
        mergeSort(arr,l,m)
        mergeSort(arr,m+1, r)
        merge(arr, l, m, r)
    else:
        return

# arr = [1,3,8,5,2,1,3,2,4]
# arr=['C','A','D']
# mergeSort(arr,0,len(arr)-1)
# print(arr)
def ascii_val(a):
    return ord(a)-64

def calcScore(arr, sol):
    for i in range(len(arr)):
        sol[i]=sum(map(ascii_val,arr[i]))

arr= []
t=int(input().strip())
for _ in range(t):
    arr.append(input().strip())
sol=[0 for _t in range(t)]
mergeSort(arr,0,len(arr)-1)
calcScore(arr,sol)
q=int(input().strip())
for _q in range(q):
    pos=arr.index(str(input().strip()))
    print(sol[pos]*(pos+1))
