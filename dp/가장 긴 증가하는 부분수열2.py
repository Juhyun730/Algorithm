import sys
import bisect
input=sys.stdin.readline


n=int(input())
l=list(map(int,input().split()))


# 원초적 방법
'''
dp=[1]*n
for i in range(1,n):
    for j in range(i):
        if l[i]>l[j]:
            dp[i]=max(dp[i],dp[j]+1)
'''
ans=[]
for i in range(n):
    idx=bisect.bisect_left(ans,l[i])
    if idx==len(ans):
        ans.append(l[i])
    else:
        ans[idx]=l[i]

print(len(ans))
