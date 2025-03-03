import sys
input=sys.stdin.readline
n=int(input())
l=[]
for _ in range(n):
    l.append(int(input()))

dp=[0]*n
dp[0]=l[0]

if n==1:
    print(dp[0])
    exit(0)
elif n==2:
    print(dp[0]+l[1])
    exit(0)
else:
    dp[1]=l[0]+l[1]
    for i in range(2,n):
        dp[i]=max(dp[i-1],dp[i-2]+l[i],dp[i-3]+l[i-1]+l[i]) # 현재포도주를 안마신다


print(dp[len(l)-1])