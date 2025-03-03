import sys
input=sys.stdin.readline

r,c=map(int,input().split())
g=[]
for i in range(r):
    g.append(list(map(str,input().strip())))
dx=[1,-1,0,0]
dy=[0,0,1,-1]
visited=[0]*26
visited[ord(g[0][0])-65]=1
mymax=0
def dfs(x,y,count):
    global mymax
    mymax=max(mymax,count)
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]

        if 0<=nx<r and 0<=ny<c and visited[ord(g[nx][ny])-65]==0:
            visited[ord(g[nx][ny])-65]=1
            dfs(nx,ny,count+1)
            visited[ord(g[nx][ny])-65]=0
dfs(0,0,1)
print(mymax)