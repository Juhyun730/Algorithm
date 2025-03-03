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

q=deque()
def bfs(x):
    q.append(x)
    while q:
        now=q.popleft()
        #print(now)
        for i in range(len(g[now])):
            if visited[g[now][i]] ==-1:
                visited[g[now][i]]=visited[now]+1
                if visited[g[now][i]]==k:
                    ans.append(g[now][i])
                elif visited[g[now][i]]<k:
                    q.append(g[now][i])

visited[x]=0
bfs(x)
ans.sort()
if len(ans)==0:
    print(-1)
else:
    for i in ans:
        print(i)

