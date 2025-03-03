import sys
from collections import deque
input=sys.stdin.readline


n,m,k,x=list(map(int,input().split()))
g=[[] for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    g[a].append(b)

ans=[]
visited=[-1]*(n+1)
visited[0]=-1
visited[x]=0
q=deque()
q.append(x)

def bfs():
    while q:
        start=q.popleft()
        for i in range(len(g[start])):
            if visited[g[start][i]]==-1:
                visited[g[start][i]]=visited[start]+1
                q.append(g[start][i])

bfs()
for i in range(n+1):
    if visited[i]==k:
        ans.append(i)
if len(ans)==0:
    print(-1)
    exit()
ans.sort()
for i in ans:
    print(i)
