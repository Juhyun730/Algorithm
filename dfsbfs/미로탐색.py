import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
g=[]
for _ in range(n):
    g.append(list(map(str,input().strip())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]
g[0][0]=1
def bfs(x,y):
    q=deque()
    q.append((x,y))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and g[nx][ny]=='1':
                g[nx][ny]=g[x][y]+1
                q.append((nx,ny))

bfs(0,0)

print(g[-1][-1])