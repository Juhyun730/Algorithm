import sys
input=sys.stdin.readline
from itertools import combinations
g=[]
team=list(combinations([i for i in range(6)],2))

for _ in range(4):
    cnt=[]
    s=list(map(int,input().split()))
    for i in range(6):
        cnt.append(s[i*3:(i+1)*3])
    g.append(cnt)

ans=[]

def check(gg):
    for a in range(6):
        for b in range(3):
            if gg[a][b]!=0:
                return False
    return True
def dfs(num,cnt):
    global flag
    if num==15:
        if check(cnt):
            flag.append(1)
        return
    nteam=team[num]
    x=nteam[0] #각각 경기하는 팀
    y=nteam[1]

    if cnt[x][0]>0 and cnt[y][2]>0: #x가 이겼을때
        cnt[x][0]-=1
        cnt[y][2]-=1
        dfs(num+1,cnt)
        cnt[x][0]+=1
        cnt[y][2]+=1      
    if cnt[x][2]>0 and cnt[y][0]>0: #x가 졌을때
        cnt[x][2]-=1
        cnt[y][0]-=1
        dfs(num+1,cnt)
        cnt[x][2]+=1
        cnt[y][0]+=1    
    if cnt[x][1]>0 and cnt[y][1]>0: #=비겼을때
        cnt[x][1]-=1
        cnt[y][1]-=1
        dfs(num+1,cnt)
        cnt[x][1]+=1
        cnt[y][1]+=1    
ans=[]
for i in range(4):
        cnt=g[i]
        flag=[]
        dfs(0,cnt)
        if 1 in flag:
            ans.append(1)
        else:
            ans.append(0)

print(*ans)