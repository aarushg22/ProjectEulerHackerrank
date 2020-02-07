#!/bin/python3

import sys

def check_palindrome(num):
    rev_num=0
    original = num
    while(num>0):
        rev_num = rev_num * 10 + (num%10)
        num//=10
    return original == rev_num

def bin_search(arr, num, min, max):
    # print(arr[min],min,arr[max],max,num)
    if num<arr[min]:
        return -1
    if num>=arr[max]:
        return max
    if num==arr[min]:
        return min
    if max==min+1:
        if num > arr[min] and num < arr[max]:
            return min
    mid = (max+min)//2
    # print(arr[mid], mid)
    if num <= arr[mid]:
        return bin_search(arr,num,min,mid)
    else:
        return bin_search(arr,num,mid+1,max)

        
def lin_search(arr,num):
    if num>arr[-1]:
        return arr[-1]
    res = arr[0]
    for x in arr:
        if num <= x:
            break
        res = x
    return res


ans = []
for a in range(100,1000):
    for b in range(100,1000):
        s = a*b
        if s>=101101:
            if check_palindrome(s):
                if s not in ans:
                    ans.append(s)
ans.sort()

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    res = lin_search(ans, n)
    print(res)
