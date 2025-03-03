import sys
from collections import deque
input=sys.stdin.readline

dx=[1,-1,0,0]
dy=[0,0,1,-1]

test=int(input())

def bfs():
    global g
    while q:
        cx,cy=q.popleft()
        for d in range(4):
            nx=cx+dx[d]
            ny=cy+dy[d]
            if 0<=nx<a and 0<=ny<b and g[nx][ny]==1:
                q.append((nx,ny))
                g[nx][ny]=0

    
for _ in range(test):
    a,b,c=map(int,input().split())
    g=[[0 for _ in range(b)] for _ in range(a)]
    q=deque()

    for i in range(c):
        x,y=map(int,input().split())
        g[x][y]=1

    num=0

    for i in range(a):
        for k in range(b):
            if g[i][k]==1:
                g[i][k]=0
                q.append((i,k))
                bfs()
                num+=1
    print(num)
