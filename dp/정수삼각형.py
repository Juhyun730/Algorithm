n=int(input())
g=[]
for i in range(n):
    l=list(map(int,input().split()))
    g.append(l)

for i in range(1,n):
    for k in range(i+1):
        if k==0 :
            g[i][k]=g[i-1][0]+g[i][k]
        elif k == i:
            g[i][k]=g[i-1][i-1]+g[i][k]
        else:
            g[i][k]=max(g[i-1][k-1],g[i-1][k])+g[i][k]

print(max(g[-1]))