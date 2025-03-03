import sys

input=sys.stdin.readline
n=int(input())

g=list(map(int,input().split()))

g.sort()

start=0
end=n-1

a=g[start]
b=g[end]
c=abs(a+b)

while start<end:
    if abs(g[start]+g[end])<c:
        c=abs(g[start]+g[end])
        a=g[start]
        b=g[end]

    if g[start]+g[end]<0:
        start+=1
    else:
        end-=1

print(a,b)
