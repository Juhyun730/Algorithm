import sys
from collections import deque
input = sys.stdin.readline

m,n,k = map(int,input().split())

g=[]
for _ in range(m):
    g.append([0]*n)

for _ in range(k):
    y1,x1,y2,x2 = map(int,input().split())
    for a in range(x1,x2):
        for b in range(y1,y2):
            g[a][b]=1
dx=[1,-1,0,0]
dy=[0,0,1,-1]
result =[]
def bfs(x,y):
    g[x][y]=1
    q=deque()
    q.append([x,y])
    ans=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y
            if 0<=nx<m and 0<=ny<n and g[nx][ny]==0:
                g[nx][ny]=1
                ans+=1
                q.append([nx,ny])
    return ans

for x in range(m):
    for y in range(n):
        if g[x][y]==0:
            result.append(bfs(x,y))

print(len(result))
print(*sorted(result))
