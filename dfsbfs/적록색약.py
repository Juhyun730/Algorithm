import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
n=int(input())
g=[list(map(str,input().strip()))for _ in range(n)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]

def dfs1(x,y,s):
    for i in range(4):
        nx=dx[i]+x
        ny=dy[i]+y
        if 0<=nx<n and 0<=ny<n and g[nx][ny]==s and visited[nx][ny]==0:
            visited[nx][ny]=1
            dfs1(nx,ny,s)

def dfs2(x,y,s):
    for i in range(4):
        nx=dx[i]+x
        ny=dy[i]+y
        if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0:
            if (g[nx][ny]=='R' or g[nx][ny]=='G')  and (s=='R' or s=='G'):
                visited[nx][ny]=1
                dfs2(nx,ny,s)

visited=[[0]*n for _ in range(n)]
ans=0
for  x in range(n):
    for y in range(n):
        if visited[x][y]==0:
            visited[x][y]=1
            dfs1(x,y,g[x][y])
            ans+=1

visited=[[0]*n for _ in range(n)]
ans2=0
for  x in range(n):
    for y in range(n):
        if visited[x][y]==0:
            visited[x][y]=1
            if g[x][y]=='B':
                dfs1(x,y,g[x][y])
            else:
                dfs2(x,y,g[x][y])
            ans2+=1           

print(ans,ans2)