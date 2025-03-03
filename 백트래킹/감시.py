import sys
import copy
input=sys.stdin.readline
n,m=map(int,input().split())
cctv=[]
g=[]
for i in range(n):
    l=list(map(int,input().split()))
    for j in range(m):
        if l[j] in [1,2,3,4,5] :
            cctv.append([i,j])
    g.append(l)
dx=[1,-1,0,0]
dy=[0,0,1,-1]
dir=[
    [],
    [[0],[1],[2],[3]],
    [[0,1],[2,3]],
    [[0,2],[0,3],[1,2],[1,3]],
    [[0,1,2],[1,2,3],[2,3,0],[0,1,3]],
    [[0,1,2,3]]
]
mymin=1e9
def cal_map(g):
    ans=0
    for x in range(n):
        for y in range(m):
            if g[x][y]==0:
                ans+=1
    return ans
def fill_map(x,y,d,g): # 현재 좌표, 방향
    for i in d:
        nx=x
        ny=y
        while 1:
            nx=nx+dx[i]
            ny=ny+dy[i]
            if 0<=nx<n and 0<=ny<m :
                if g[nx][ny]==0:
                    g[nx][ny]=-1#방문 처리
                if g[nx][ny]==6:
                    break
            else:
                break
def dfs(i,g):
    global mymin
    if i==len(cctv):
        mymin=min(mymin,cal_map(g))
        return
    else:
        x = cctv[i][0]
        y = cctv[i][1]
        temp=copy.deepcopy(g)
        for d in dir[g[x][y]]:
            fill_map(x,y,d,temp) # cctv 감시영역 채워넣기
            dfs(i+1,temp) #채워넣은 영역 기반으로 dfs 돌리기
            temp=copy.deepcopy(g)
        
                
dfs(0,g)
    
print(mymin)