import sys
from collections import deque
input=sys.stdin.readline
n,l,r=map(int,input().split())
g=[]
for i in range(n):
    g.append(list(map(int,input().split())))
dx=[1,-1,0,0]
dy=[0,0,1,-1]

#인구이동이 가능한지 탐색하고, 
def bfs(x,y):
    q=deque()
    q.append([x,y])
    visited[x][y]=1
    nq=[[x,y]]
    while q:
        x,y=q.popleft()
        for d in range(4):
            nx=x+dx[d]
            ny=y+dy[d]
            if 0<=nx<n and 0<=ny<n: #탐색 가능한 방향일때
                if l<=abs(g[x][y]-g[nx][ny]) and r>=abs(g[x][y]-g[nx][ny]) and visited[nx][ny]==0: #범위가 충족하면
                    nq.append([nx,ny])
                    #print(nx,ny)
                    q.append([nx,ny])
                    visited[nx][ny]=1
    return nq

# 인구이동시킴
def move_people(nq):
    n_sum=0
    for x,y in nq:
        n_sum+=g[x][y]
    n_sum//=len(nq)
    for x,y in nq:
        g[x][y]=n_sum
    return
ans=0
while True:
    flag=False
    visited=[[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if not visited[x][y]:
                nq=bfs(x,y)
                if len(nq)>1:
                    move_people(nq)
                    flag=True
    if flag==True:
        ans+=1
    if flag==False:
        break
print(ans)
