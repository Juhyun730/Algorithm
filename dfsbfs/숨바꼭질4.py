import sys
from collections import deque
input=sys.stdin.readline
sys.setrecursionlimit(100001)
n,k=map(int,input().split())

visited=[-1]*(100001)
visited[n]=0
cnt=[n]
prev = [-1] * 100001  # 방문경로를 추적할 배열
q=deque([n])
mintime=1e9

def bfs():
    global mylist, count
    while q:
        x=q.popleft()
        if x==k:
            break
        for i in [x-1,x+1,2*x]:
            if 0<=i<100001 and visited[i]==-1 :
                visited[i]=visited[x]+1
                prev[i]=x # i를 방문했을때 이전 위치인 x 기록
                q.append(i)
bfs()
path=[]
cur=k
while cur!=-1:
    path.append(cur)
    cur=prev[cur]
print(visited[k])
print(' '.join(map(str,path[::-1])))