import heapq

n = int(input())
l = []

for _ in range(n):
    heapq.heappush(l,int(input()))

# 가장 작은 두 묶음에 대해서 효율적으로 계속 합쳐나가야함

mysum=0

while len(l)>1: # 힙에 하나 혹은 0개 만 남았을떄까지
    a=heapq.heappop(l)#현재 가장 작은 값
    b=heapq.heappop(l) #현재 두번째로 작은 값
    mysum+=(a+b)
    heapq.heappush(l,(a+b))

print(mysum)