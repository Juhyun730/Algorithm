import sys
input=sys.stdin.readline

c,n=map(int,input().split()) #c명, 도시개수
city=[]
for i in range(n):
    city.append(list(map(int,input().split())))

#3원을 들여서 5명이 늘어남
dp=[100000000]*1000
dp[0]=0
for k in range(n):
    n_cost=city[k][0]
    n_people=city[k][1]
    for i in range(n_people,c+100):
        dp[i]=min(dp[i],min(dp[i-n_people:i])+n_cost)

print(min(dp[c:]))
