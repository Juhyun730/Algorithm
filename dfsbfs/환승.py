import sys
from collections import deque

input = sys.stdin.readline

n, k, m = map(int, input().split())

station = [[] for _ in range(n + 1)]
hyper = [[] for _ in range(m + 1)]

for i in range(1, m + 1):
    l = list(map(int, input().split()))
    hyper[i] = l
    for j in l:
        station[j].append(i)  # 각각의 역이 몇 번째 하이퍼튜브에 있는지 기록

q = deque()
q.append((1, 1))  # 현재 탐색 역, 레벨 (현재 몇 번만에 도달했는지)
visited_station = [-1] * (n + 1)
visited_hyper = [False] * (m + 1)

visited_station[1] = 1  # 첫 역 방문 처리

while q:
    ns, nl = q.popleft()
    
    if ns == n:  # 목표 역에 도달한 경우
        print(nl)
        exit(0)
    
    for hyper_tube in station[ns]:
        if not visited_hyper[hyper_tube]:
            visited_hyper[hyper_tube] = True  # 하이퍼튜브 방문 처리
            
            for next_station in hyper[hyper_tube]:
                if visited_station[next_station] == -1:
                    visited_station[next_station] = nl + 1
                    q.append((next_station, nl + 1))
    
print(-1)  # 목표 역에 도달할 수 없는 경우