import sys

input=sys.stdin.readline

n,d,k,c=map(int,input().split())

g=[]
for i in range(n):
    g.append(int(input()))

cnt=0
start=0

while start<n:
    if start + k<=(n):
        if c not in g[start:start+k]:
            eat=len(set(g[start:start+k]))+1
        else:
            eat=len(set(g[start:start+k]))

        if cnt==0:
            cnt=eat
        elif cnt<eat:
            cnt=eat
    else:
        s=g[start:]+g[:k-len(g[start:])]
        if c not in s:
            eat=len(set(s))+1
        else:
            eat=len(set(s))

        if cnt==0:
            cnt=eat
        elif cnt<eat:
            cnt=eat
    start+=1

print(cnt)