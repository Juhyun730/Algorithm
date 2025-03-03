import sys

input=sys.stdin.readline

n,m=map(int,input().split())
l=list(map(int,input().split()))
l=sorted(l)
# 245


def dfs():#i= 0~n
    if len(cnt)==m:
        print(' '.join(map(str, cnt)))
        return
    for x in range(n):
        if visited[x]==0:
            visited[x]=1
            cnt.append(l[x])
            dfs()
            cnt.pop()
            visited[x]=0

cnt=[]
for a in range(n):
    visited=[0]*(n)
    visited[a]=1
    cnt.append(l[a])
    dfs()
    cnt=[]
