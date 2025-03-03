import sys
import heapq
input=sys.stdin.readline


n,m,k,x=list(map(int,input().split()))
g=[[] for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    g[a].append(b)
dis=[1e9]*(n+1)
dis[x]=0
q=[[dis[x],x]]
def dijkstra():
    while q:
        now_d, now_x=heapq.heappop(q)
        for i in range(len(g[now_x])):
            if dis[g[now_x][i]]>1+now_d:
                dis[g[now_x][i]]=1+now_d
                heapq.heappush(q,[dis[g[now_x][i]],g[now_x][i]])
dijkstra()
ans=[]

for i in range(len(dis)):
    if dis[i]==k:
        ans.append(i)
if len(ans)==0:
    print(-1)
else:
    for i in ans:
        print(i)