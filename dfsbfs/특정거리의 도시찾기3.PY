import sys
from collections import deque
input=sys.stdin.readline

n,m,k,x = map(int,input().split())
g=[[] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    g[a].append(b)

result=[]
visited=[0]*(n+1)
def bfs(start):
    q=deque()
    q.append([start,0])
    visited[start]=1
    while q:
        now,dis = q.popleft()
        if dis < k:
            for i in g[now]:
                if visited[i]==0:
                    visited[i]=1
                    q.append([i,dis+1])
        elif dis == k:
            result.append(now)
bfs(x)
if len(result)==0:
    print(-1)
else:
    result.sort()
    for i in result:
        print(i)
