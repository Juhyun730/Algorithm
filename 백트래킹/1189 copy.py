import sys

input=sys.stdin.readline

r,c,k=map(int,input().split())
graph=[]
for i in range(r):
    graph.append(list(input()))


dx=[1,-1,0,0]
dy=[0,0,-1,1]

ans=0
def dfs(x,y,dis):
    global ans
    for i in range(4):
        nx=dx[i]+x
        ny=dy[i]+y
        if nx==0 and ny==c-1 and dis+1==k:
            ans+=1
            
        if 0<=nx<r and 0<=ny<c:
            if graph[nx][ny]=='.':
                graph[nx][ny]='T'
                dis+=1
                print(nx,ny,dis)
                dfs(nx,ny,dis)
                dis-=1
                graph[nx][ny]='.'


graph[r-1][0]='T'
dfs(r-1,0,1)
print(ans)
