import sys
input=sys.stdin.readline

n=int(input())

dp=[[0]*3 for _ in range(n)]
g=[]
for i in range(n):
    g.append(list(map(int,input().split())))
dp[0]=g[0]

for i in range(1,n):
    dp[i][0]=min(dp[i-1][1],dp[i-1][2])+g[i][0]
    dp[i][1]=min(dp[i-1][0],dp[i-1][2])+g[i][1]
    dp[i][2]=min(dp[i-1][0],dp[i-1][1])+g[i][2]


print(min(dp[n-1]))

