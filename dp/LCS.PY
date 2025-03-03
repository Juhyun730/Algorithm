import sys
from itertools import combinations
input=sys.stdin.readline

l1=list(map(str,input().strip()))
l2=list(map(str,input().strip()))

dp=[[0]*(len(l2)+1) for _ in range(len(l1)+1)]

for i in range(1,len(l1)+1):
    for j in range(1,len(l2)+1):
        if l1[i-1]==l2[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])

print(dp[-1][-1])
