n=int(input())

dis=list(map(int,input().split())) #노드간 거리
node=list(map(int,input().split())) # 리터당 주유가격

# 주유비가 적은곳에서 가장 많이 주유하기

oil=node[0]
now=dis[0]*node[0]

for i in range(1,n-1):
    if node[i]<oil:
        oil=node[i]
        now+=oil*dis[i]
    else:
        now+=oil*dis[i]


print(now)