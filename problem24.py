"""
See problem24_fact.py for working solution, this is just some experimental code
"""

import math

def insert(a, segment):
    segment = segment[::-1]
    ln = len(segment)
    inserted_ind = 0
    max=(segment[-1],ln-1)
    chk=1
    if ln>1:
        for j in range(ln-1):
            if segment[j] > a:
                if segment[j] < max[0]:
                    max = (segment[j],j)
    # print(max[0],max[1])
    # print(segment[0:max[1]],segment[max[1]+1:-1])
    segment = max[0]+(segment[0:max[1]]+segment[max[1]+1:])
    if ln>1:
        for i in range(1,ln):
            if a<segment[i]:
                return segment[:i]+a+segment[i:]
    # if chk:
    #     max = a,
    return segment+a

def nextPerm(s):
    for i in range(len(s)-1,0,-1):
        if s[i-1] < s[i]:
            segment = s[i:]
            # print(s[i-1],segment)
            new = insert(s[i-1], segment)
            # print(new)
            sol = s[0:i-1] + new
            return sol
    return None

curr = 'abcdefghijklm'
for x in range(math.factorial(6)):
    print(curr,x)
    if curr is None: break
    curr = nextPerm(curr)


#
# t = int(input().strip())
# for a0 in range(t):
#     n = int(input().strip())-1
#     perm_str = 'abcdefghijklm'
#     if n > 24:
#         nf=0
#         for nf in range(13):
#             if math.factorial(nf)>n: break
#         num = n
#         useful_seg = perm_str[-nf:]
#         nf = math.factorial(nf-1)
#         it=0
#         while((num-nf)>0):
#             num -= nf
#             it+=1
#         fixed = useful_seg[it]
#         useful_seg = useful_seg[:it]+useful_seg[it+1:]
#         # print(fixed, useful_seg)
#         # num-=1
#         while(num>0):
#             useful_seg = nextPerm(useful_seg)
#             num-=1
#         print(perm_str[:-nf]+fixed+useful_seg)
#     else:
#         while(n>0):
#             perm_str = nextPerm(perm_str)
#             n-=1
#         print(perm_str)
