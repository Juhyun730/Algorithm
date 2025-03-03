n=int(input())

'''dp=[0]*100000

dp[1]=1
dp[2]=1
dp[3]=1
dp[5]=1
count=4
i=2
while count<=n:
    if dp[i]==1:
        dp[i*2]=1 #2
        dp[i*3]=1
        dp[i*5]=1
        i+=1
        count+=3

count=0
idx=0
while count<n:
    if dp[idx]==1:
        count+=1
    idx+=1
print(idx-1)'''

dp=[0]*n
dp[0]=1
i2=i3=i5=0
next2,next3,next5=2,3,5

for i in range(1,n):
    dp[i]=min(next2,next3,next5)
    if dp[i]==next2:
        i2+=1
        next2=dp[i]*2
    if dp[i]==next3:
        i3+=1
        next3=dp[i]*3
    if dp[i]==next5:
        i5+=1
        next5=dp[i]*5
print(dp[n-1])