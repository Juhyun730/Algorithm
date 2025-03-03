n=int(input())

g=[[]]
for i in range(n):
    g.append(list(map(int,input().split())))
dp=[0]*(n+1)

for i in range(1,n+1): # 하루하루 지날떄마다
    dp[i]=max(dp[i],dp[i-1])
    if i+g[i][0]-1<=n:# 만약 i번째 날에 상담을 할 경우, n일 전에 끝나면
        #끝나는 날에
        dp[i+g[i][0]-1]=max(dp[i+g[i][0]-1],g[i][1]+dp[i-1],dp[i+g[i][0]-2])

print(max(dp))
