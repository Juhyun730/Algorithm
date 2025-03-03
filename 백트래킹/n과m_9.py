import sys

input=sys.stdin.readline

n,m=map(int,input().split())
l=list(map(int,input().split()))

l=sorted(l)
# 245


def dfs(x):
    global visited, check
    if len(cnt)==m:
        print(' '.join(map(str, cnt)))
        return
    for k in range(x,n):
        if visited[k]==0 and check!=l[k]:
            check=l[k]
            cnt.append(l[k])
            visited[k]=1
            dfs(x+1)
            cnt.pop()
            visited[k]=0

cnt=[]

for i in range(len(l)):
    check=l[i]
    
    visited=[0]*n
    visited[i]=1
    cnt.append(l[i])
    dfs(i)
    cnt=[]