import sys

from collections import deque

sys.setrecursionlimit(10**6)

input=sys.stdin.readline
n,m=map(int,input().split())

g=[]
for i in range(n):
    g.append(list(map(int,input().strip())))


q=deque()
dx=[1,-1,0,0]
dy=[0,0,-1,1]



def bfs(x,y):
    q.append((x,y))

    while q:
        cx,cy=q.popleft()
        for i in range(4):
            nx=cx+dx[i]
            ny=cy+dy[i]
            if 0<=nx<n and 0<=ny<m :
                if g[nx][ny]==1:
                    g[nx][ny]=g[cx][cy]+1
                    q.append((nx,ny))
                    
    return g[n-1][m-1]



print(bfs(0,0))