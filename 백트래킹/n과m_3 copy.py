import sys

input=sys.stdin.readline

n,m=map(int,input().split())

visited=[0]*(n+1)
cnt=[]
def dfs():
    if len(cnt)==m:
        print(*cnt)
        return
    for i in range(1,n+1):
        cnt.append(i)
        dfs()
        cnt.pop()
dfs()
