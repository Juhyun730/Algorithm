import sys
input=sys.stdin.readline
sys.setrecursionlimit(100001)
n,k=map(int,input().split())
minc=1e9
visited=[-1]*(100001)
visited[n]=0
from collections import deque
mintime=1e9
q=deque([n])
count=0
while q:
    x=q.popleft()
    if x==k:
        if visited[x]<mintime:
            mintime=visited[x]
            count=1
        elif visited[x] == mintime:
            count += 1

    for i in [x-1,x+1,2*x]:
        if 0<=i<100001:
            if visited[i]==-1 or visited[i]>=visited[x]+1:
                visited[i]=visited[x]+1
                q.append(i)
print(mintime)
print(count)