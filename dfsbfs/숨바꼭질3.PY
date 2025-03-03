import sys
from collections import deque

input=sys.stdin.readline

n,k=map(int,input().split())
q=deque()

q.append(n)

visited=[-1]*100001
visited[n]=0

def bfs():

    while q:
        x=q.popleft()
        if x==k:
            return visited[x]
        for i in (x-1,x+1,2*x):
            if 0<=i<=100000 and (visited[i]==-1 or visited[i]>visited[x]):
                if i==2*x:
                    visited[i]=visited[x]
                    q.appendleft(i)
                else:
                    visited[i]=visited[x]+1
                    q.append(i)
        

mymax=bfs()
print(mymax)
'''import sys
input = sys.stdin.readline

n,k = map(int, input().split())

cq = [[n,0]]
MAX = 100001
check = [False for _ in range(MAX+1)]
time = 0
check[n] = True
while True:
    nq = []
    for i,t in cq:
        check[i] = True
        if i==k:
            print(t)
            exit(0)
        if i*2 <= MAX and not check[i*2]:
            nq.append([i*2,t])
            check[i*2] = True
        if i-1 >= 0 and not check[i-1]:
            nq.append([i-1,t+1])
            check[i-1] = True
        if i+1 <= MAX and not check[i+1]:
            nq.append([i+1,t+1])
            check[i+1] = True
    if not nq:
        break
    cq = nq'''

