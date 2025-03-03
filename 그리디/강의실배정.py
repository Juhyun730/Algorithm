import sys
input=sys.stdin.readline
import heapq 
n=int(input())

l=[]
for _ in range(n):
    l.append(list(map(int,input().split())))

l.sort()

last_time=[l[0][1]]

for i in range(1,n):
    if l[i][0] >= last_time[0]: #남은 강의실중에서 가장빨리 끝나는 시간
        heapq.heappop(last_time)
    heapq.heappush(last_time,l[i][1])

print(len(last_time))