import sys
import heapq
input=sys.stdin.readline

n,d=map(int,input().split())
g=[[] for _ in range(d+1)]
dist=[1e9] * (d+1)

for i in range(d+1):
    g[i].append([i+1,1])

for i in range(n):
    a,b,c=map(int,input().split())
    if b>d:
        continue
    g[a].append([b,c])

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    dist[start]=0
    while q:
        x,y=heapq.heappop(q)
        if x<dist[y]:
            continue
        for i in g[y]:
            cur=x+i[1]
            if dist[i[0]]>cur:
                dist[i[0]]=cur
                heapq.heappush(q,(cur,i[0]))
dijkstra(0)
print(dist[d])


        
