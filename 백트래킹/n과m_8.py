import sys

input=sys.stdin.readline

n,m=map(int,input().split())
l=list(map(int,input().split()))
l=sorted(l)
# 245


def dfs(x):
    if len(cnt)==m:
        print(' '.join(map(str, cnt)))
        return
    for i in range(x,n):
        cnt.append(l[i])
        dfs(i)
        cnt.pop()

cnt=[]
dfs(0)