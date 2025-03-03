import sys
from collections import deque
input =sys.stdin.readline
sys.setrecursionlimit(10**7)
n,m=map(int,input().split())

dx=[0,0,1,-1,-1,-1,1,1]
dy=[1,-1,0,0,-1,1,-1,1]

g=[]
for i in range(n):
    g.append(list(map(int,input().split())))

def bfs():
    global mysum
    while q:
        xx,yy=q.popleft()
        for i in range(8):
            nx=dx[i]+xx
            ny=dy[i]+yy
            if 0<=nx<n and 0<=ny<m and g[nx][ny]==0 and visited[nx][ny]==0: #상어가 아니야
                visited[nx][ny]=visited[xx][yy]+1
                q.append((nx,ny))
            elif 0<=nx<n and 0<=ny<m and g[nx][ny]==1 : 
                return visited[xx][yy]



realsum=0
for x in range(n):
    for y in range(m):
        if g[x][y]==0:
            visited=[[0]*m for _ in range(n)]
            visited[x][y]=1
            q=deque()
            q.append((x,y))
            mysum=bfs()
            realsum=max(realsum,mysum)

print(realsum)