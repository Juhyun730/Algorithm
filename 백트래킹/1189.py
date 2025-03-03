import sys

input=sys.stdin.readline

r,c,k=map(int,input().split())
graph=[]
for i in range(r):
    graph.append(list(input()))


dx=[1,-1,0,0]
dy=[0,0,-1,1]


sum=0

def dfs(x,y,d):
    global sum
    if d==k and x==0 and y==(c-1):
        sum+=1
    else:
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<r and 0<=ny<c and graph[nx][ny]=='.':        
                graph[nx][ny]='T'
                dfs(nx,ny,d+1)
                graph[nx][ny]=='.'
dfs(r-1,0,1)
# 정답
print(sum)
            