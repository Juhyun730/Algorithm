import sys

input=sys.stdin.readline

n=int(input())
m=int(input())
g=[]
for i in range(m):
    a,b,c=map(int, input().split())
    g.append([c,a,b])
g.sort()
p=[i for i in range(n+1)]
def find(x):
    #print(x,p[x])
    if p[x]!=x: #부모노드가 본인과 다르면
        p[x]=find(p[x]) #부모노드의 부모노드를 찾기
    return p[x]

def union(a,b):
    x=find(a)
    y=find(b)
    if x!=y:
        if x<y:
            p[y]=x
        else:
            p[x]=y
ans=0
#print(p)
for i in range(m):
    c,a,b=g[i]
    #print("######################")
    if find(a)!=find(b):
        union(a,b)
        ans+=c
    #print(p)

print(ans)
