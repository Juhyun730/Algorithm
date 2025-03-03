import sys
from collections import deque 

input=sys.stdin.readline

r,c,k=map(int,input().split())

g=[]
for i in range(r):
    g.append(list(input().strip()))

dx=[1,-1,0,0]
dy=[0,0,1,-1]
visited=[[0]*c for _ in range(r)]
mysum=0

def bfs(x,y,d):
    global mysum
    q=deque()
    q.append((x,y,d))
    while q:
        x,y,d=q.popleft()
        if x==0 and y== c-1 and d==k:
            mysum+=1
            continue
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<r and 0<=ny<c and g[nx][ny]=='.':
                if dx[i]==-1 or dy[i]==1:
                    q.append((nx,ny,d+1))


bfs(r-1,0,1)
print(mysum)


