import sys
import heapq
input=sys.stdin.readline
n=int(input())
bus=int(input())
g=[[] for _ in range(n+1)]
for _ in range(bus):
    a,b,c=map(int,input().split())
    g[a].append([b,c])
start,end=map(int,input().split())

def djkstra(x):
    distance=[1e9]*(n+1)
    distance[x]=0
    q=[]
    heapq.heappush(q,[0,x])
    while q:
        dis,node=heapq.heappop(q)
        if dis>distance[node]:
            continue
        for neighbor,d in g[node]:
            if dis+d < distance[neighbor]:
                distance[neighbor]=dis+d
                heapq.heappush(q,[distance[neighbor],neighbor])
    return distance
distance=djkstra(start)
print(distance[end])