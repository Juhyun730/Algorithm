import sys

input=sys.stdin.readline

n,m=map(int,input().split())
l=list(map(int,input().split()))
l=sorted(l)
# 245


def dfs(x):
    if len(cnt)==m:
        print(' '.join(map(str, cnt)))
        return
    for i in range(x,len(l)):
        if visited[i]==0:
            visited[i]=1
            cnt.append(l[i])
            dfs(i+1)
            visited[i]=0
            cnt.pop()


visited=[0]*n
cnt=[]
dfs(0)
