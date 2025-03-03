from collections import deque
import sys
input=sys.stdin.readline

m,n=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(input().strip()))

dx=[1,-1,0,0]
dy=[0,0,1,-1]


visited=[[0]*m for _ in range(n)]
wsum=0
bsum=0

def bfs(x,y,s):
    q=deque()
    global wsum, bsum
    q.append((x,y))
    visited[x][y]=1
    count=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==s and visited[nx][ny]==0:
                q.append((nx,ny))
                count+=1
                visited[nx][ny]=1
    if s=='W':
        wsum+=count**2
    elif s=='B':
        bsum+=count**2


for a in range(n):
    for b in range(m):
        if visited[a][b]==0:
            bfs(a,b,graph[a][b])

print(wsum, bsum)