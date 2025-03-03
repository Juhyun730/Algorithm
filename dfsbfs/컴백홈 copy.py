import sys
from collections import deque 
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

r,c,k=map(int,input().split())

g=[]
for i in range(r):
    g.append(list(input().strip()))

dx=[1,-1,0,0]
dy=[0,0,1,-1]

ans=0
cnt=1
g[r-1][0]='T'
def dfs(x,y,cnt):
    global ans
    if x==0 and y==c-1:
        if cnt==k:
            ans+=1
            return

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<r and 0<=ny<c :
            if g[nx][ny]=='.':
                g[nx][ny]=='T'
                dfs(nx,ny,cnt+1)
                g[nx][ny]=='.'

dfs(r-1,0,1)

print(ans)