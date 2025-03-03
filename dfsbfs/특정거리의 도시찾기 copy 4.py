import sys
from collections import deque
input=sys.stdin.readline
n,m,k,x=list(map(int,input().split()))
g=[[] for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    g[a].append(b)

ans=[]
visited=[0]*(n+1)
def bfs(x):
    q=deque()
    q.append([x,0])
    while q:
        x,dis=q.popleft()
        if dis==k:
            ans.append(x)
        for neighbor in g[x]:
            if visited[neighbor]==0:
                visited[neighbor]=1
                q.append([neighbor,dis+1])
bfs(1)
if ans:
    ans.sort()
    for i in ans:
        print(i)
else:
    print(-1)
