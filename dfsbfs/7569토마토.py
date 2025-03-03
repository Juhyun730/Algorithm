import sys
from collections import deque
input=sys.stdin.readline

m,n,h=map(int,input().split())
g=[[] for _ in range(h)]
q=deque()
tonum=0
for i in range(h):
    for a in range(n):
        l=list(map(int,input().split()))
        for tomato in range(len(l)):
            if l[tomato]==1:
                q.append([i,a,tomato])
            if l[tomato]!=-1:
                tonum+=1
        g[i].append(l)

d=[[0,-1,0],[0,1,0],[0,0,-1],[0,0,1],[1,0,0],[-1,0,0]]
day=-1
def bfs(nq):
    cq=deque()
    while nq:
        box,x,y=nq.popleft()
        for dir in d:
            nbox=dir[0]+box
            nx=dir[1]+x
            ny=dir[2]+y
            if 0<=nbox<h and 0<=nx<n and 0<=ny<m:
                if g[nbox][nx][ny]==0:
                    g[nbox][nx][ny]=1
                    cq.append([nbox,nx,ny])
    return cq
if len(q)==(h*m*n):
    print(0)
    exit()

while q:
    q=bfs(q)
    day+=1
    

count=0
for a in range(h):
    for b in range(n):
        for c in range(m):
            if g[a][b][c]==1:
                count+=1
            if g[a][b][c]==0:
                print(-1)
                exit()

if count==tonum:
    print(day)
else:
    print(-1)