import sys
from collections import deque
import copy
input=sys.stdin.readline

n,m=map(int,input().split())
gg=[]
for i in range(n):
    gg.append(list(map(int,input().split())))


cnt_count=0
#좌표 세개 선정해서 1로 바꾸고 -> 감염 후(bfs) -> 0인 칸 개수 구하기

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs(x,y):
    q=deque()
    q.append((x,y))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0:
                visited[nx][ny]=1
                if g[nx][ny]!=1:
                    g[nx][ny]=2
                    q.append((nx,ny))

def count():
    cnt=0
    for i in range(n):
        for j in range(m):
            if g[i][j]==0:
                cnt+=1
    return cnt
           
idx=[]

for x in range(n):
    for y in range(m):
        if gg[x][y]==0:
            #g[x][y]=1
            idx.append([x,y])
            for x1 in range(x,n):
                for y1 in range(m):
                    if gg[x1][y1]==0:
                        if [x1,y1] not in idx:
                        #g[x1][y1]=1ss
                            idx.append([x1,y1])
                            for x2 in range(x1,n):
                                for y2 in range(m):
                                    if gg[x2][y2]==0:
                                        if [x2,y2] not in idx:
                                            idx.append([x2,y2])

                                            g=copy.deepcopy(gg)
                                            for ix,iy in idx:
                                                g[ix][iy]=1
                                            #g[x2][y2]=1
                                            visited=[[0 for i in range(m) ] for i in range(n)]
                                            for xx in range(n):
                                                for yy in range(m):
                                                    if g[xx][yy]==2 and visited[xx][yy]==0:
                                                        bfs(xx,yy)
                                            cnt_count=max(cnt_count,count())
                                            idx.pop()
                            idx.pop()

            idx.pop()
print(cnt_count)