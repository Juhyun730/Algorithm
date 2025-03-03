import sys
input=sys.stdin.readline
from collections import deque

n,k=map(int,input().split())
g=[]
cq=deque()
for _ in range(n):
    g.append(list(map(int,input().split())))

s,x,y=map(int,input().split())

for num in range(1,k+1):
    for i in range(n):
        for j in range(n):
            if g[i][j]==num:
                cq.append((i,j,num))
x=x-1
y=y-1
#k개의 바이러스
dx=[-1,1,0,0]
dy=[0,0,-1,1]


def bfs(cx,cy,virus):
    for t in range(4):
        nx=dx[t]+cx
        ny=dy[t]+cy
        if 0<=nx<n and 0<=ny<n:
            if g[nx][ny]==0:
                g[nx][ny]=virus
                nq.append((nx,ny,virus))

for second in range(1,s+1):
    nq=deque()
    while cq:
        cx,cy,virus=cq.popleft()
        bfs(cx,cy,virus)
    cq=nq


'''for second in range(1,s+1):
    for virus in range(1,k+1):
        visited=[[-1]*n for _ in range(n)]
        for cx in range(n):
            for cy in range(n):
                if g[cx][cy]==virus and visited[cx][cy]==-1:
                    visited[cx][cy]=1
                    bfs(cx,cy,virus)
'''
print(g[x][y])

