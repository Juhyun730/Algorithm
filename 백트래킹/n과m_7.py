import sys

input=sys.stdin.readline

n,m=map(int,input().split())
l=list(map(int,input().split()))
l=sorted(l)
# 245


def dfs(i):
    if len(cnt)==m:
        print(' '.join(map(str, cnt)))
        return
    for i in range(n):
        cnt.append(l[i])
        dfs(i+1)
        cnt.pop()

for a in range(n):
    cnt=[]
    cnt.append(l[a])
    dfs(a)
