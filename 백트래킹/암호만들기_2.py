import sys 
input=sys.stdin.readline

l,c=map(int,input().split())
arr=list(map(str,input().split()))
arr.sort()
vowels = {'a', 'e', 'i', 'o', 'u'}

def dfs(s,num_c,num_v,depth):
    if len(s)==l and num_c>=2 and num_v>=1:
        print(s)
        return
    for i in range(depth,c):
        s+=arr[i]
        if arr[i] in vowels:
            dfs(s,num_c,num_v+1,i+1)
        else:
            dfs(s,num_c+1,num_v,i+1)
        s=s[:-1]

dfs('',0,0,0)