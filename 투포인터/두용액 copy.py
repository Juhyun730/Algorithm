import sys

input=sys.stdin.readline
n=int(input())

g=list(map(int,input().split()))

g.sort()
#print(g)
l=0
r=n-1
mymin=1e10
x=0
y=1
while l<r:
    mymin=min(mymin,abs(g[l]+g[r]))
    if mymin==abs(g[l]+g[r]):
        x=l
        y=r
    if g[l]+g[r]<0: #음수일때
        l=l+1
    elif g[l]+g[r]==0:
        break
    else:
        r=r-1

print(g[x],g[y])
