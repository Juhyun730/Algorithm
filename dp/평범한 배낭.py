import sys
input=sys.stdin.readline

n,k=map(int,input().split()) #물건 개수, 백팩 무게
l=[[0,0]]

for _ in range(n):
    w,v=map(int,input().split())
    l.append([w,v])
dp=[[0]*(k+1) for _ in range(n+1)] # 최대 가치를 저장할 테이블; 행:물건, 열: 무게

for i in range(1,n+1): #물건 순회
    for j in range(1,k+1): #무게 순회
        if j < l[i][0]: # 물건의 무게가 담을수있는 무게보다 클경우
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-l[i][0]]+l[i][1])
print(dp[n][k])
'''for i in range(n):
    w,v=map(int,input().split()) # 무게 , 가치
    l.append([w,v])

# v의 합이 최대가 되도록
dp=[[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,k+1):
        if j < l[i][0]: # 물건의 무게가 배낭의 임시 용량보다 더 커서, 못담는 경우
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-l[i][0]] + l[i][1])

print(dp[n][k])'''

# for i in range(n):
#     w,v=map(int,input().split())
#     l.append([w,v])

# #무게는 적게, 가치는 많이
# dp=[0]*(k+1)
# #어떤걸 어디서부터 업데이트할지 디피테이블 잘 선정하기
# for w,v in l:
#     for i in range(k,w-1,-1):
#         dp[i]=max(dp[i],dp[i-w]+v)

# print(dp[k])
