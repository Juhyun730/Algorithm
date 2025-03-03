import sys
input=sys.stdin.readline

n=int(input())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))

dp=[[0]*n for i in range(n)]
dp[0][0]=1

#현재 위치에서 오른쪽으로, 아래쪽으로 탐색
print(dp)
print(l)
for x in range(n):
    for y in range(n):
        if l[x][y]!=0 and dp[0][0]!=0:
            if x+l[x][y]<n: # 오른쪽으로 갈 수 있다면
                dp[x+l[x][y]][y]+=dp[x][y]
            if y+l[x][y]<n:
                dp[x][y+l[x][y]]+=dp[x][y]

print(dp[-1][-1])