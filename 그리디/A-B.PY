import sys
from collections import deque
input=sys.stdin.readline

a,b=map(int,input().split())

'''def bfs(x):
    global b
    count=1
    q=deque()
    q.append((x,count))
    while q:
        x,count=q.popleft()
        if x==b:
            return count
        if 2*x<=b:
            q.append((2*x,count+1))
        if int(str(x)+'1')<=b:
            q.append((int(str(x)+'1'),count+1))
ans=bfs(a)
if ans is None:
    print(-1)
    exit()
print(bfs(a))'''
count=1
while b>a:
    if b%10==1:
        b=b//10
    elif b%2==0:
        b=b//2
    else:
        print(-1)
        exit()
    count+=1
if b==a:
    print(count)
else:
    print(-1)