import sys

input=sys.stdin.readline

n,m=map(int,input().split())
l=list(map(int,input().split()))
l.sort()

def dfs():
    if len(cnt)==m:
        print(' '.join(map(str,cnt)))
        return
    for x in range(n):
        if visited[x]==0:
            visited[x]=1
            cnt.append(l[x])
            dfs()
            visited[x]=0
            cnt.pop()
    
cnt=[]
for i in range(len(l)):
    visited=[0]*n
    cnt.append(l[i])
    visited[i]=1
    dfs()
    cnt=[]
