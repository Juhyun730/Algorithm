import sys
from itertools import combinations
from collections import deque
input=sys.stdin.readline

g=[[] for _ in range(5)]
for i in range(5):
    g[i]=list(map(str,input().strip()))
position=[(i,j) for i in range(5) for j in range(5)]

dx=[1,-1,0,0]
dy=[0,0,-1,1,]

def is_connected(com):
    q=deque([com[0]])
    visited=set([com[0]])
    count=1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if (nx,ny) in com and (nx,ny) not in visited:
                visited.add((nx,ny))
                q.append((nx,ny))
                count+=1
    return count==7

ans=0
for com in combinations(position,7):
    s=0
    for x,y in com:
        if g[x][y]=='S':

             
            s+=1
    if s>=4:
        if is_connected(com):
            ans+=1

print(ans)