'''import sys

input=sys.stdin.readline

g=[]
n=int(input())

for i in range(n):
    s=list(map(int,input().split()))
    g.append(s)

l=[]

for i in range(n):
    for t in range(n):
        if len(l)<n:
            l.append(g[i][t])
        else:
            if l[0]<g[i][t]:
                l[0]=g[i][t]

        l.sort()
            
print(l[0])'''
import sys
import heapq
input=sys.stdin.readline

n = int(input())
graph = [8, 9, 13, 1, 12]
heapq.heapify(graph)
print(graph)
heapq.heappop(graph)
print(graph)