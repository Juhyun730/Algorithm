import sys
input=sys.stdin.readline

n,k=map(int,input().split())
l=list(map(int,input().split()))

dp=[1e9] * (k + 1) # 카페인만큼 테이블 만들기
dp[0] = 0  # 카페인 양 0을 만들기 위해선 커피를 0개 사용
for coffee in l:
    for i in range(k,coffee,-1):
        dp[i]=min(dp[i],dp[i-coffee]+1)
if dp[k]==1e9:
    print(-1)
else:print(dp[k])