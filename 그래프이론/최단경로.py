import sys
input=sys.stdin.readline

n=int(input())
m=int(input())
g=[[1e9]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,c=map(int,input().split())
    g[a][b]=min(c,g[a][b])
for i in range(1,n+1):
    g[i][i]=0

for mid in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            cnt=g[i][mid]+g[mid][j]
            g[i][j]=min(cnt,g[i][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if g[i][j]==1e9:
            g[i][j]=0
for i in range(1,n+1):
    for j in g[i][1:]:
        print(j,end=' ')
    print('')