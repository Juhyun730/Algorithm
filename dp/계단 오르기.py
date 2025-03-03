import sys
input=sys.stdin.readline


n=int(input())
l=[0]
for _ in range(n):
    l.append(int(input()))

dp=[0]*(n+1)
dp[n]=l[n]
dp[n-1]=dp[n]+l[n-1]
dp[n-2]=l[n-2]+l[n]

flag=1

for i in range(n-3,-1,-1):
    # if flag!=2:
    #     a=dp[i+1]+l[i]
    #     b=dp[i+2]+l[i]
    #     dp[i]=max(dp[i+1]+l[i],dp[i+2]+l[i])

    #     if dp[i] == dp[i+1]+l[i]:
    #         flag=2
    #     elif dp[i]== dp[i+2]+l[i]:
    #         flag=1

    # elif flag==2:
        dp[i]=max(dp[i+2]+l[i],dp[i+3]+l[i+1]+l[i])
        # if dp[i] == dp[i+3]+l[i+1]+l[i]:
        #     flag=2
        # elif dp[i]== dp[i+2]+l[i]:
        #     flag=1
            
if len(l)==2:
    print(l[-1])
else: 
    print(max(dp))