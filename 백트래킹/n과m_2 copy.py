import sys

input=sys.stdin.readline

n,m=map(int,input().split())

visited=[0]*(n+1)

def dfs(now):
    if len(cnt)==m:
        print(*cnt)
        return
    for j in range(now+1,n+1):
        if visited[j]==0:
            visited[j]=1
            cnt.append(j)
            dfs(j)
            cnt.remove(j)
            visited[j]=0
for i in range(1,n+1):
    cnt=[]
    visited[i]=1
    cnt.append(i)
    dfs(i)
    

    




