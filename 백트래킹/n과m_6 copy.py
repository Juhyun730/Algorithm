import sys

input=sys.stdin.readline

n,m=map(int,input().split())
l=list(map(int,input().split()))
l=sorted(l)
cnt=[]
visited=[0]*n

def dfs(x):
    if len(cnt)==m:
        print(*cnt)

    for i in range(x,n):
        if visited[i]==0:
            visited[i]=1
            cnt.append(l[i])
            dfs(i+1)
            cnt.pop()
            visited[i]=0
dfs(0)