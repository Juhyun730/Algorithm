import sys
from collections import deque
input=sys.stdin.readline


n,m,k,x=list(map(int,input().split()))
g=[[] for _ in range(n+2)]
for i in range(m):
    a,b=map(int,input().split())
    g[a].append(b)

visited=[0]*(n+1)
dist=[0]*(n+1)
q=deque()
def bfs(x):
    q.append(x)
    visited[x]=1
    while q:
        now=q.popleft()
        for i in g[now]:
            if visited[i]==0:
                visited[i]=1
                dist[i]=dist[now]+1
                q.append(i)

bfs(x)

if k in dist:
    l=[]
    for i in range(n+1):
        if dist[i]==k:
            print(i)
else:
    print(-1)

