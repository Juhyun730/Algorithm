import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split())

g=[]
for i in range(n):
    g.append(list(map(int,input().split())))
dx=[-1,-1,-1,0,0,1,1,1] 
dy=[-1,0,1,1,-1,-1,0,1]

visited=[[-1]*m for _ in range(n)]

def bfs(x,y):
    q=deque()
    q.append((x,y))
    flag=True
    while q :
        x,y=q.popleft()
        for i in range(8):
            nx=dx[i]+x
            ny=dy[i]+y
            if 0<=nx<n and 0<=ny<m :
                if g[nx][ny]>g[x][y]:
                    flag=False
                elif g[nx][ny]==g[x][y] and visited[nx][ny]==-1:
                    visited[nx][ny]=1
                    q.append((nx,ny))

    return flag
        



ans=0
for a in range(n):
    for b in range(m):
        if visited[a][b]==-1:
            visited[a][b]=1
            flag=bfs(a,b)
            if flag:
                ans+=1

print(ans)



