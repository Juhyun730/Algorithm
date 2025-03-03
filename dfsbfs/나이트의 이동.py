import sys
from collections import deque
input=sys.stdin.readline
nt=int(input())
d=[[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1]]

def bfs(x,y,tx,ty,now):
    q=deque()
    q.append([x,y,now])
    visited[x][y]=1
    while q:
        x,y,now=q.popleft()
        if x==tx and y==ty:
            return now
        for i in d:
            nx=x+i[0]
            ny=y+i[1]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0:
                visited[nx][ny]=1
                q.append([nx,ny,now+1])


for _ in range(nt):
    n=int(input()) # n*n
    x,y=map(int,input().split())
    tx,ty=map(int,input().split())
    visited=[[0]*n for _ in range(n)]
    now=bfs(x,y,tx,ty,0)
    print(now)


