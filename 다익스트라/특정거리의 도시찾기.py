import sys
import heapq
input=sys.stdin.readline
n,m,k,x=map(int,input().split())
dist=[1e9]*(n+1)
g=[[] for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    g[a].append((b,1))

def dk(start):
    q=[]
    heapq.heappush(q,(0,start))
    dist[start]=0
    while q:
        di,node=heapq.heappop(q)
        if di>dist[node]:
            continue
        for i in g[node]:
            cur=di+i[1]
            #print(i)
            if cur <dist[i[0]]:
                dist[i[0]]=cur
                heapq.heappush(q,(cur,i[0]))

dk(x)
if k in dist:
    for i in range(n+1):
        if dist[i]==k:
            print(i)
else:
    print(-1)
