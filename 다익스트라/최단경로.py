import heapq
v,e=map(int,input().split())
start=int(input())
g=[[] for _ in range(v+1)]
for i in range(e):
    a,b,c=map(int,input().split())
    g[a].append([b,c])

dist=[999999]*(v+1)
dist[start]=0
q=[[dist[start],start]]

def dijkstra():
    while q:
        now_d,now_n=heapq.heappop(q)
        for n,d in g[now_n]:
            distance=d+now_d
            if dist[n]>distance:
                dist[n]=distance
                heapq.heappush(q,[dist[n],n])
dijkstra()
for i in range(1,v+1):
    if dist[i]==999999:
        print('INF')
    else:
        print(dist[i])