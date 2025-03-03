import sys
from copy import deepcopy
input =sys.stdin.readline
sys.setrecursionlimit(10**7)

dy=[0,0,-1,-1,-1,0,1,1,1]
dx=[0,-1,-1,0, 1, 1,1,0,-1]


g=[[] for _ in range(4)]

for i in range(4):
    l=list(map(int,input().split()))
    for k in range(0,8,2):
        g[i].append([l[k],l[k+1]])


mysum=g[0][0][0]
g[0][0][0]=-1

l=[]


#물고기의 회전
def fish1(n):
    for x in range(4):
        for y in range(4):
            if g[x][y][0]==n:#현재 돌 숫자를 찾았을 때
                fish2(x,y)
                return

#물고기 위치 이동-     
def fish2(i,j):
    cnt=0
    start_dir=g[i][j][1]
    for t in range(start_dir,9):
        nx=i+dx[t]
        ny=j+dy[t]
        if 0<=nx<4 and 0<=ny<4:
            if g[nx][ny][0]==-1:
                continue

            else:
                g[nx][ny][0],g[nx][ny][1],g[i][j][0],g[i][j][1] = g[i][j][0],t,g[nx][ny][0],g[nx][ny][1]
                cnt=1
                break
    if cnt==0:
        for t in range(1,start_dir):
            nx=i+dx[t]
            ny=j+dy[t]
            if 0<=nx<4 and 0<=ny<4:
                if g[nx][ny][0]==-1:
                    continue
                else:
                    g[nx][ny][0],g[nx][ny][1],g[i][j][0],g[i][j][1] = g[i][j][0],t,g[nx][ny][0],g[nx][ny][1]
                    cnt=1
                    break
                
def dfs(x,y):
    global mysum,l,g
    for n in range(1,17):
        fish1(n)
    # for i in range(len(g)):
    #     print(g[i])
    dir=g[x][y][1] #상어의 방향
    nx=x+dx[dir]
    ny=y+dy[dir]

    while 0<=nx<4 and 0<=ny<4:
    #if 0<=nx<4 and 0<=ny<4:
        
        fish=g[nx][ny][0]
        if fish>0:
            mysum+=fish

            c=deepcopy(g)
            g[nx][ny][0]=-1 #상어이동
            g[x][y][0]=0 #상어가 있던자리 초기화
            g[x][y][1]=0 #상어가 있던자리 초기화

            dfs(nx,ny)

            g=c
            mysum-=fish

        nx=nx+dx[dir]
        ny=ny+dy[dir]
        

    l.append(mysum)

    return

dfs(0,0)
'''for n in range(1,17):
    fish1(n)
for i in range(len(g)):
    print(g[i])'''

print(max(l))