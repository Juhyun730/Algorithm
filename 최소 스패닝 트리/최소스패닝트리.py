import sys
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
v,e=map(int,input().split())
edges=[]

for i in range(e):
    a,b,c=map(int,input().split())
    edges.append([c,a,b])
edges.sort()
parent=[i for i in range(v+1)]

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def union(x,y):
    x=find(x)
    y=find(y)
    if x>y:
        parent[x]=y
    else:
        parent[y]=x

ans=0

for cost, a, b in edges:
    if find(a) != find(b):
        union(a,b)
        ans+=cost
print(ans)