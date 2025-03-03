import sys
from collections import deque
input=sys.stdin.readline

m,n=map(int,input().split())
g=[]
to_num=0
tomato=deque()
for i in range(n):
    l=list(map(int,input().split()))
    g.append(l)
    for k in range(m):
        if l[k]==1:
            tomato.append([i,k])
            to_num+=1
        elif l[k]==0:
            to_num+=1

dx=[1,-1,0,0]
dy=[0,0,1,-1]

if len(tomato)==(n*m):
    print(0)
    exit(0)

tomato2=deque()

#하루지났을때 퍼지고, 그다음날 1토마토 기준으로 또 퍼지고

def bfs(tomato):
    tomato2=deque()
    while tomato:
        x,y=tomato.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and g[nx][ny]==0:
                tomato2.append([nx,ny])
                g[nx][ny]=1
    return tomato2

tomato2=bfs(tomato)
day=0
while tomato2:
    tomato2=bfs(tomato2)
    day+=1
count=0
for x in range(n):
    for y in range(m):
        if g[x][y]==1:
            count+=1
if count==to_num:
    print(day)
else:
    print(-1)