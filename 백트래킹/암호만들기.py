import sys
input=sys.stdin.readline

l,c=map(int,input().split())
arr=list(map(str,input().split()))
arr.sort()
vowels = {'a', 'e', 'i', 'o', 'u'}
visited=[0]*c

# a c i s t w

def dfs(s,i,num_v,num_c):
    if len(s)==l:
        if num_v>=1 and num_c>=2:
            print(s)
            return
    for i in range(i,c):
        s+=arr[i]
        if arr[i] in vowels:
            dfs(s,i+1,num_v+1,num_c)
        else:
            dfs(s,i+1,num_v,num_c+1)
        s=s[:-1]

dfs('',0,0,0)